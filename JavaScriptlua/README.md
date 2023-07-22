const LuaModule = require('./LuaModule');

const moduleInstance = new LuaModule('path to dll file LUA');

moduleInstance.execute_file('path to lua script');

moduleInstance.__del__();
