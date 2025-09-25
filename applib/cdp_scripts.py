script1 = r"""
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


script2 = """
                const getContext = HTMLCanvasElement.prototype.getContext;
                HTMLCanvasElement.prototype.getContext = function(type, ...args) {
                    return getContext.apply(this, [type, ...args]);
                };

                const toDataURL = HTMLCanvasElement.prototype.toDataURL;
                HTMLCanvasElement.prototype.toDataURL = function(...args) {
                    // слегка модифицируем данные
                    return toDataURL.apply(this, args).replace("0", "1");
                };

                const getParameter = WebGLRenderingContext.prototype.getParameter;
                WebGLRenderingContext.prototype.getParameter = function(parameter) {
                    // можно подменить vendor / renderer
                    if (parameter === 37445) return "Intel Inc.";  // UNMASKED_VENDOR_WEBGL
                    if (parameter === 37446) return "Intel Iris OpenGL Engine"; // UNMASKED_RENDERER_WEBGL
                    return getParameter.apply(this, [parameter]);
                };
            """