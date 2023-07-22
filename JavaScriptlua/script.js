// script.js
const LuaModule = require('./LuaModule');

const luaFileInput = document.getElementById('luaFileInput');
const dllFileInput = document.getElementById('dllFileInput');
const executeButton = document.getElementById('executeButton');

executeButton.addEventListener('click', () => {
    if (!luaFileInput.files || !luaFileInput.files[0] || !dllFileInput.files || !dllFileInput.files[0]) {
        alert('Пожалуйста, выберите файл и DLL');
        return;
    }

    const moduleInstance = new LuaModule(dllFileInput.files[0].path);
    try {
        moduleInstance.execute_file(luaFileInput.files[0].path);
    } catch (error) {
        console.error(error);
    } finally {
        moduleInstance.__del__();
    }
});
