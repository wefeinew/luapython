import ctypes

class LuaModule:
    def __init__(self, dll_path):
        self.lua = ctypes.CDLL(dll_path)
        self.lua.luaL_newstate.restype = ctypes.c_void_p
        self.lua.luaL_dofile.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.lua.lua_tolstring.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]

        self.L = self.lua.luaL_newstate()
        
        # Load the standard Lua libraries
        self.lua.luaL_openlibs(self.L)

    def execute_file(self, file_path):
        result = self.lua.luaL_dofile(self.L, file_path.encode())
        
        if result != 0:
            string_buffer = ctypes.create_string_buffer(128)
            self.lua.lua_tolstring(self.L, -1, string_buffer)
            raise RuntimeError(f"Script execution error: {string_buffer.value.decode()}")

    def __del__(self):
        self.lua.lua_close(self.L)
