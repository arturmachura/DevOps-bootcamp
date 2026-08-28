Podstawowe:

git init — tworzy repo
git clone <url> — kopiuje repo
git status — stan zmian
git add <plik> — dodaje do staging
git commit -m "..." — zapisuje commit
git push — wysyła zmiany
git pull — pobiera zmiany
git branch — lista branchy
git checkout -b <branch> — nowy branch
git merge <branch> — łączy branch
git log — historia commitów
git diff — pokazuje różnice

Bardziej wyrafinowane:

git rebase <base> — przenosi commity
git rebase -i <base> — interaktywny rebase
git reset --hard <commit> — cofa wszystko
git reset <plik> — odznacza plik
git revert <commit> — cofa commitem
git commit --amend — poprawia ostatni commit
git reflog — historia HEAD
git stash — chowa zmiany tymczasowo
git cherry-pick <commit> — przenosi jeden commit
git clean -n — pokazuje śmieci
git remote add <name> <url> — dodaje zdalne repo
git fetch — pobiera bez merge
git push --force — wymusza push
git tag — oznacza wersję
git bisect — szuka buga binarnie