from applib.custom_chrome_options import CustomChromeOptions
from selenium import webdriver



class Browser:
    def __init__(self) -> None:
        self._driver = webdriver.Chrome(options=CustomChromeOptions().setup())
        # --- Реалистичный JS, который выполняется до кода страницы ---
        script = r"""
        (() => {
        // Подмена navigator.webdriver
        try {
            Object.defineProperty(navigator, 'webdriver', { get: () => false, configurable: true });
        } catch (e) {}

        // Подмена navigator.languages
        try {
            Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'], configurable: true });
        } catch (e) {}

        // Реалистичные "плагины"
        try {
            const fakePlugins = [
            {
                name: 'Chrome PDF Plugin',
                filename: 'internal-pdf-viewer',
                description: 'Portable Document Format'
            },
            {
                name: 'Widevine Content Decryption Module',
                filename: 'widevinecdm',
                description: ''
            }
            ];

            // Сделаем объект похожим на PluginArray
            const pluginArray = {
            length: fakePlugins.length,
            item: function(i) { return fakePlugins[i]; },
            namedItem: function(name) { return fakePlugins.find(p => p.name === name) || null; }
            };

            // добавим числовые индексы (0,1,...)
            for (let i = 0; i < fakePlugins.length; i++) {
            pluginArray[i] = fakePlugins[i];
            }

            // toString / Symbol.toStringTag чтобы выглядеть естественнее
            Object.defineProperty(pluginArray, Symbol.toStringTag, { value: 'PluginArray' });

            Object.defineProperty(navigator, 'plugins', {
            get: () => pluginArray,
            configurable: true
            });
        } catch (e) {}

        // Доп. — иногда проверяют permissions API (пример: разрешения для notifications)
        try {
            const origQuery = window.navigator.permissions && window.navigator.permissions.query;
            if (origQuery) {
            const fakeQuery = function(parameters) {
                if (parameters && parameters.name === 'notifications') {
                return Promise.resolve({ state: Notification.permission });
                }
                return origQuery(parameters);
            };
            // Переопределяем метод
            Object.defineProperty(window.navigator, 'permissions', {
                get: () => ({ query: fakeQuery }),
                configurable: true
            });
            }
        } catch (e) {}

        })();
        """

        # Добавляем скрипт, который будет выполняться на каждом новом документе
        resp = self._driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})
        # в ответе обычно есть 'identifier' или 'scriptId' — сохраним как script_id
        script_id = resp.get("identifier") or resp.get("scriptId")
        print("added script id:", script_id)

       

    def open(self, url: str) -> None:
        """
        Open url.
        """
        self._driver.get(url=url)

        # # можно проверить из браузера:
        # print(self._driver.execute_script("return navigator.webdriver;"))       # ожидаем False
        # print(self._driver.execute_script("return navigator.languages;"))      # ожидаем ['en-US','en']
        # print(self._driver.execute_script("return navigator.plugins.length;")) # ожидаем >0



    @property
    def driver(self):
        return self._driver


    def close(self) -> None:
        self._driver.quit()


# https://www.instagram.com/aasdjjfjfkfk/
# https://www.instagram.com/geek_culture_store/
# https://www.instagram.com/hildegard.debondt/
