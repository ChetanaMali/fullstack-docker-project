const express = require("express");
const axios = require("axios");

const app = express();

app.use(express.urlencoded({extended:true}));
app.use(express.json());

app.set("view engine","ejs");

app.get("/", (req,res)=>{
    res.render("form");
});

     
app.post("/submit", async (req,res)=>{

    try{

        await axios.post(
            "http://backend:5000/submit",
            req.body
        );

        res.redirect("/success");

    }catch(error){

        res.send(
            `Error: ${error.message}`
        );
    }
});

app.get("/success",(req,res)=>{
    res.render("success");
});

app.listen(3000, ()=>{
    console.log("Frontend running");
});