#include <iostream>
#include <lua.hpp>

int main() {
    // Инициализация интерпретатора Lua
    lua_State* L = luaL_newstate();
    
    // Загрузка стандартных библиотек Lua
    luaL_openlibs(L);

    // Загрузка и выполнение скрипта Lua из файла
    if (luaL_dofile(L, "script.lua") != LUA_OK) {
        std::cerr << "Ошибка выполнения скрипта: " << lua_tostring(L, -1) << std::endl;
    }
    
    // Освобождение ресурсов интерпретатора Lua
    lua_close(L);

    return 0;
}
