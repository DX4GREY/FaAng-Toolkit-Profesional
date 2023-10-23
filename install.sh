doTermux() {
	rm -rf $PREFIX/bin/faang
	mkdir -p $PREFIX/share/faang
	cp -r -f modules/* $PREFIX/share/faang
	chmod +x $PREFIX/share/faang/main.py
	ln -s $PREFIX/share/faang/main.py $PREFIX/bin/faang
}
doGnuLinux() {
	sudo rm -rf /usr/local/bin/faang
	sudo mkdir -p /usr/share/faang
	sudo cp -r -f modules/* /usr/share/faang
	sudo chmod +x /usr/share/faang/main.py
	sudo ln -s /usr/share/faang/main.py /usr/local/bin/faang
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
	echo -e "[*] Done. just run : faang"
}

doInstall() {
	echo -n "[*] Installing faang..."
	if [ "$(uname -o)" = "Android" ]; then
		doTermux
	else
		doGnuLinux
	fi
	echo -e "[DONE]"
	installRequirements
}
doInstall