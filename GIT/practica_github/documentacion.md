# Practica guiada  
+ Aprendiendo sobre git y github  
+ Repasando uso básico de la consola para gestión de directorios  
+ Usando markdown again ;)  
  
**Empezamos la practica en la carpeta donde irá el repositorio**
```bash
mkdir prueba_git  
cd prueba_git  

nano texto.txt 
nano script.sh
```
<!-- Hemos creado el directorio y escrito con nano los dos archivos dentro de él-->

**Creamos el repostorio local** 
<!-- En mi caso lo creo y ya le cambio el nombre de master a main y lo revertí tras comprobar el cambio -->
```bash
git init

git branch -m main
git status
On branch main
Your branch is up to date with 'origin/main'.

git branch -m master
git status
On branch master
Your branch is up to date with 'origin/main'.
```  
<!-- Podemos ver que en el git status cambia el nombre de master a main y viceversa -->
**Una vez probado el iniciarlo y renombrar añadimos un archivo de los dos que aun no forman parte del propio repositorio**  
```bash
git add script.sh
git status
On branch master
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   script.sh

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        texto.txt

git commit -m "confirmación inicial"
git status
On branch master
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)
```
<!-- Si quisieramos añadir todos de golpe serviría con hacer git add . De momento hemos probado a solo meter uno de los dos para entender el funcionamiento de el comando -->  
**Ahora si añadimos tambien el otro y vamos comprobando**  
```bash
$ git add texto.txt
$ git commit -m “añadido archivo texto.txt” 
$ git status
On branch master
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)
```
**Tras la modificacion de texto.txt ejecutamos:**  
```bash
$ git status
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   texto.txt

no changes added to commit (use "git add" and/or "git commit -a")
$ git add texto.txt
$ git status
On branch master
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   texto.txt
$ git status -> (tras añadir 5)
On branch master
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   texto.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   texto.txt
```

**Comandos útiles para la informacion:**  
```bash
$ git show

commit 20149420164236a0d6b8f543c93478649d9e14a8 (HEAD -> master)
Author: PabloSAlonso <santanaalonsopablo@gmail.com>
Date:   Sat Nov 1 19:48:11 2025 +0100

    añadido archivo texto.txt

diff --git a/GIT/practica_github/texto.txt b/GIT/practica_github/texto.txt
new file mode 100644
index 0000000..15bf608

$ git log
Author: PabloSAlonso <santanaalonsopablo@gmail.com>
Date:   Sat Nov 1 19:48:11 2025 +0100

    añadido archivo texto.txt

commit 2c23ffa48a996f3cbe8d83eb092e87af8daa2e86
Author: PabloSAlonso <santanaalonsopablo@gmail.com>
Date:   Sat Nov 1 19:45:44 2025 +0100
```
**Comando para mostrar diferencias entre una version y la anterior y probandolo:**  
```bash
git diff -> (Por ejemplo los cambios en texto.txt:)
warning: in the working copy of 'GIT/practica_github/texto.txt', LF will be replaced by CRLF the next time Git touches it
diff --git a/GIT/practica_github/texto.txt b/GIT/practica_github/texto.txt
index d92e49a..ea169a0 100644
--- a/GIT/practica_github/texto.txt
+++ b/GIT/practica_github/texto.txt
@@ -1,5 +1,5 @@
 uno
 dos
-tres
$ git commit -a -m "Probando diff"
```
<!-- Ejecutamos el commit asi para no hacer add porque en este cambio de version no hemos añadido archivos -->

**Para evitar archivos que no interese guardar, se utiliza el .gitignore, que es un archivo dentro del propio directorio de trabajo**


```bash
nano .gitignore *.class Ahora git ignora los archivos terminados por .class
```
**Para comprobarlo, al añadirle archivos al directorio se ejecuta:**

```bash
ls -a 
git add .
git commit -m "Añadiendo fuentes en java y archivos importantes"
``` 

**Tags y gestión de versiones (git tag y git checkout)**

```bash
git tag v0.7 

git tag v0.3 

git log --oneline 

git checkout v0.3 

git checkout main 

```
**Ramas**

```bash
git branch Prueba 

git switch Prueba 

git branch 

git merge Prueba
```
**Eliminar y quitar de seguimiento**
```bash
git rm 

git reset HEAD *.class

```
**Repositorios remotos: Github**
```bash
git clone direccion

git push -u origin main 

git push 
```
<!-- Cuando haces un pull o push del origin main es exclusivamente cuando la primera vez que ejecutas ese comando en remoto, despues del primero procederás a ejecutarlo normal hasta que vuelvas a cambiar tu zona de trabajo -->





