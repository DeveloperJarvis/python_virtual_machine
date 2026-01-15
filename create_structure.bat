@echo off

REM Root directory
@REM set ROOT=log_pattern_detection_tool
set ROOT=.

REM Create directories if they do not exist
call :create_folder "%ROOT%"
call :create_folder "%ROOT%\config"
call :create_folder "%ROOT%\docs"
call :create_folder "%ROOT%\examples"
call :create_folder "%ROOT%\logs"
call :create_folder "%ROOT%\src"
call :create_folder "%ROOT%\tests"
call :create_folder "%ROOT%\tools"
call :create_folder "%ROOT%\vm"
call :create_folder "%ROOT%\vm\bytecode"
call :create_folder "%ROOT%\vm\control"
call :create_folder "%ROOT%\vm\core"
call :create_folder "%ROOT%\vm\errors"
call :create_folder "%ROOT%\vm\memory"
call :create_folder "%ROOT%\vm\stack"
call :create_folder "%ROOT%\vm\utils"

REM Create files only if they do not exist
REM Python source files (with header)
call :create_py_file "%ROOT%\setup.py"

call :create_py_file "%ROOT%\run_example.py"

call :create_py_file "%ROOT%\config\_init__.py"
call :create_py_file "%ROOT%\config\config.py"

call :create_py_file "%ROOT%\tests\__init__.py"
call :create_py_file "%ROOT%\tests\test_stack.py"
call :create_py_file "%ROOT%\tests\test_bytecode.py"
call :create_py_file "%ROOT%\tests\test_execution.py"
call :create_py_file "%ROOT%\tests\test_control_flow.py"

call :create_py_file "%ROOT%\tools\_init__.py"
call :create_py_file "%ROOT%\tools\assembler.py"
call :create_py_file "%ROOT%\tools\disassembler.py"

call :create_py_file "%ROOT%\vm\__init__.py"
call :create_py_file "%ROOT%\vm\bytecode\__init__.py"
call :create_py_file "%ROOT%\vm\bytecode\loader.py"
call :create_py_file "%ROOT%\vm\bytecode\parser.py"
call :create_py_file "%ROOT%\vm\bytecode\instructions.py"
call :create_py_file "%ROOT%\vm\control\__init__.py"
call :create_py_file "%ROOT%\vm\control\flow.py"
call :create_py_file "%ROOT%\vm\control\callstack.py"
call :create_py_file "%ROOT%\vm\core\engine.py"
call :create_py_file "%ROOT%\vm\core\runtime.py"
call :create_py_file "%ROOT%\vm\core\vm.py"
call :create_py_file "%ROOT%\vm\errors\__init__.py"
call :create_py_file "%ROOT%\vm\errors\exceptions.py"
call :create_py_file "%ROOT%\vm\memory\__init__.py"
call :create_py_file "%ROOT%\vm\memory\namespace.py"
call :create_py_file "%ROOT%\vm\memory\constants.py"
call :create_py_file "%ROOT%\vm\stack\__init__.py"
call :create_py_file "%ROOT%\vm\stack\stack.py"
call :create_py_file "%ROOT%\vm\stack\frame.py"
call :create_py_file "%ROOT%\vm\utils\__init__.py"
call :create_py_file "%ROOT%\vm\utils\debug.py"

REM Non-Python files (empty)
call :create_file "%ROOT%\docs\bytecode.md"
call :create_file "%ROOT%\docs\execution_model.md"

call :create_file "%ROOT%\examples\simple_arithmetic.bc"
call :create_file "%ROOT%\examples\conditionals.bc"
call :create_file "%ROOT%\examples\function_call.bc"
@REM call :create_file "%ROOT%\examples\function_call_alter.bc"

call :create_file "%ROOT%\logs\vm.log"

call :create_file "%ROOT%\requirements.txt"
call :create_file "%ROOT%\README.md"
call :create_file "%ROOT%\LICENSE"

echo Folder structure created (existing files and folders were preserved).
goto :eof

REM -------------------------------------------
REM Create folders if does not exist
REM -------------------------------------------

:create_folder
if not exist "%~1" (
    mkdir "%~1"
)

REM -------------------------------------------
REM Create empty file if it does not exist
REM -------------------------------------------

:create_file
if not exist "%~1" (
    type nul > "%~1"
)

exit /b

REM -------------------------------------------
REM Create python file with GPL header
REM -------------------------------------------
:create_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the Python Virtual Machine Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # Python Virtual Machine - Parse bytecode and execute instructions ^(custom VM^)
echo #                       Skills: parsing, bytecode, stack machines, interpreters
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo.
) > "%FILEPATH%"

exit /b