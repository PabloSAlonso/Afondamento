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
<!-- En mi caso lo creo y ya le cambio el nombre de master a main  y lo revertí tras comprobar el cambio -->
```bash
git init
git branch -m main
git branch -m master
```  
**Una vez probado el iniciarlo y renombrar añadimos un archivo de los dos que aun no forman parte del propio repositorio**  
```bash
git add script.sh
git status
git commit -m "confirmación inicial"
git status
```
<!-- Si quisieramos añadir todos de golpe serviría con hacer git add . De momento hemos probado a solo meter uno de los dos para entender el funcionamiento de el comando -->  
**Ahora si añadimos tambien el otro y vamos comprobando**  
```bash
$ git add texto.txt
$ git commit -m “añadido archivo texto.txt” 
$ git status
```
**Tras la modificacion de texto.txt ejecutamos:**  
```bash
$ git status
$ git add texto.txt
$ git status
```
**Comandos útiles para la informacion:**  
```bash
$ git show
$ git log
```
**Comando para mostrar diferencias entre una version y la anterior y probandolo:**  
```bash
git diff
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





