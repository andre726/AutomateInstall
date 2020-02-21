#!/usr/bin/env bash
sudo apt install -y zsh git curl
sudo chsh -s /usr/bin/zsh andre
# Installation des fonts
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.0.0/Hack.zip
unzip Hack.zip -d hackfonts && rm Hack.zip
sudo mv hackfonts /usr/share/fonts/
fc-cache -v # rafraichi le cache des polices.
fc-list | grep -i hack # vérifier la présence et prise en charge de la police.
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/zsh-completions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k


#credit Michael hertens