#!/bin/bash
pathName="faang"
mainFile="main.py"

doTermux() {
	rm -rf $PREFIX/bin/$pathName
	mkdir -p $PREFIX/share/$pathName
	cp -r -f modules/* $PREFIX/share/$pathName
	chmod +x $PREFIX/share/$pathName/$mainFile
	ln -s $PREFIX/share/$pathName/$mainFile $PREFIX/bin/$pathName
}
doGnuLinux() {
	sudo rm -rf /usr/local/bin/$pathName
	sudo mkdir -p /usr/share/$pathName
	sudo cp -r -f modules/* /usr/share/$pathName
	sudo chmod +x /usr/share/$pathName/*
	sudo ln -s /usr/share/$pathName/$mainFile /usr/local/bin/$pathName
}
installRequirements() {
	echo -n "[*] Checking python if installed..."
	if [ -x "$(command -v python)" ]; then
		echo -e "[INSTALLED]"
	else
		echo -e "[NOT INSTALLED]"
		echo -e "Installation aborted..."
		echo -e "Please install python then try again..."
		exit
	fi
	
	echo -e "[*] Installing dependencies..."
	pip install -r requirements.txt
	echo -e "[*] Done. just run : $pathName"
}

doInstall() {
	echo -n "[*] Installing $pathName..."
	if [ "$(uname -o)" = "Android" ]; then
		doTermux
	else
		doGnuLinux
	fi
	echo -e "[DONE]"
	installRequirements
}
doInstall