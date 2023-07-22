#include <iostream>
#include <lua.hpp>

int main() {
    
    lua_State* L = luaL_newstate();
    
    luaL_openlibs(L);
    
    if (luaL_dofile(L, "script.lua") != LUA_OK) {
        std::cerr << "Script execution error: " << lua_tostring(L, -1) << std::endl;
    }

    lua_close(L);

    return 0;
}
