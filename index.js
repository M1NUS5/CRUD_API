//Importar las bibliotecas cargar el modulo
const express = require('express')
//Importar el modulo path
const path= require('path')
//Creacion de la instancia
const app=express()
//Definir el puerto escuchar las solicitudes
const port = 3000

//creacion
app.get('/',(reg, res)=>{
    res.sendFile(path.join(__dirname,'index.html'));
});

//Iniciar el servidor
app.listen(port,()=>{
    console.log(`Servidor ejecutandose en http://localhost:${port}`)
})