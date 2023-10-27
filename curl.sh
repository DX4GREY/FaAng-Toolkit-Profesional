repo="FaAng-Toolkit-Profesional"
username="dx4grey"

install_termux() {
    pkg update
    pkg upgrade
    pkg install git
    git clone https://github.com/$username/$repo
    cd $repo
    bash install.sh
    cd ../
    rm -rf $repo
}
install_linux() {
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install git
    git clone https://github.com/$username/$repo
    cd $repo
    bash install.sh
    cd ../
    sudo rm -rf $repo
}

detect_platform() {
    platform=$(uname -o)
    echo -e "[*] Start installation on $platform"
    case $platform in
        "Android")
            install_termux
            ;;
        "GNU/Linux")
            install_linux
            ;;
        *)
            echo "[*] Unsupported platform: $platform"
            ;;
    esac
}
detect_platform
