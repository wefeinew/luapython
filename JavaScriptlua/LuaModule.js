class LuaModule {
    constructor(dll_path) {
        this.lua = require('ffi').Library(dll_path);
        this.lua.luaL_newstate.restype = 'void *';
        this.lua.luaL_dofile.argtypes = ['void *', 'char *'];
        this.lua.lua_tolstring.argtypes = ['void *', 'int', 'void *'];
        this.L = this.lua.luaL_newstate();
        
        this.lua.luaL_openlibs(this.L);
    }
    execute_file(file_path) {
        const result = this.lua.luaL_dofile(this.L, Buffer.from(file_path));
        if (result !== 0) {
            const string_buffer = Buffer.alloc(128);
            this.lua.lua_tolstring(this.L, -1, string_buffer);
            throw new Error(`Script execution error: ${string_buffer.toString()}`);
        }
    }
    __del__() {
        this.lua.lua_close(this.L);
    }
}
