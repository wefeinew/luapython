To include the "lua script utils" library in your project and use it in your code, do the following:

First unzip the "lua script utils" library and place it in your project directory.

Import the desired module from the "lua script utils" library into your code:

from lua script utils import luarun Use the luarun function to execute a Lua script. Specify the path to your Lua script as an argument to the function:

luarun("path/to/script.lua") This will run a Lua script in your Python project.

Alternatively, you can also use the luascriptcompilation function to compile a Lua script into a bytecode file. Specify the path to the output file and the path to the Lua script as function arguments:

from lua script utils import luascriptcompilation

luascriptcompilation("output-script", "path/to/script.lua") This will compile the Lua script to bytecode and save it to the specified output file.

Another option is to use the wluarun function, which allows you to run a Lua script with better integration between Python and Lua, passing variables and data between them. Use the following code:

from lua script utils import wluarun

wluarun("path/to/script.lua") Note that "path/to/script.lua" in the code snippets above should be replaced with the actual path to your Lua script file. It is important that it is not installed via pip, you need to safely add it to your project

to install libs use module:

from lua script utils import search_luarocks

search_luarocks("You module name")


---------------------------------------------------------------------------------------------------
requisition libraries:
pip install requests beautifulsoup4 lupa, ctypes  (ctypes no optional)
