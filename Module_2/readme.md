Podstawowe:

pwd — bieżący katalog
ls / ls -a — lista plików
cd <dir> — zmiana katalogu
mkdir <dir> — nowy katalog
touch <plik> — nowy plik
rm <plik> / rm -r <dir> — usuwanie
cp / mv — kopiuj / przenieś
cat <plik> — pokaż zawartość
history — historia komend
clear — czyści terminal
uname -a — info o systemie
sudo <cmd> — uprawnienia roota
su - <user> — zmiana użytkownika
sudo apt install <pakiet> — instalacja pakietu
vim <plik> — edycja pliku

Bardziej wyrafinowane:

chmod 755 <plik> — uprawnienia numerycznie
chmod g+x <plik> — uprawnienia symbolicznie
chown user:group <plik> — zmiana właściciela
sudo useradd -G <grupa> <user> — dodaje do grupy
sudo usermod -g <grupa> <user> — zmienia grupę
history | grep sudo — filtruje historię
cat plik | grep wzorzec — szuka wzorca
polecenie > plik — nadpisuje wynik
polecenie >> plik — dopisuje wynik
for param in "$@"; do ... done — pętla po parametrach
if [ ... ]; then ... fi — warunek w skrypcie
function nazwa() { ... } — funkcja w skrypcie
export ZMIENNA=wartość — zmienna środowiskowa
printenv | grep <fraza> — filtruje zmienne
ssh-keygen -t rsa — generuje klucz SSH
ssh -i klucz user@host — łączy z kluczem
ping / nslookup — diagnostyka sieci