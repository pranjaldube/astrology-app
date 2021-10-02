const express = require("express") ;
const bodyParser = require("body-parser") ;
const override = require("method-override");
const app = express() ;
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/indiatodaydb', {
  useNewUrlParser: true,
  useUnifiedTopology: true
})

app.use(express.json()) ;
app.use(express.static("public")) ;
app.use(bodyParser.urlencoded({extended: true})) ;
app.use(override("_method")) ; 

const bannerSchema = new mongoose.Schema({
    nameOfBanner: String ,
    schemeDescription : String , 
    images: {
        thumbnail: String,
        large: String
    },
    redirectUrl: String,
})
const Banner = mongoose.model("Banners" , bannerSchema) ;

const horoscopeSchema = new mongoose.Schema({
    name: String,
    img: String,
    imges:{
        thumbnail : String,
        large: String
    },
    detailURL: String , 
})
const Horoscope = mongoose.model("Horoscopes" , horoscopeSchema) ;

const astroSchema = new mongoose.Schema({
    astrologer: String,
    img: String,
    firstName: String,
    lastName: String,
    aboutAstrologer : String,
    experience: String,
    rating: Number,
    languages: Array,
    costPerMin: Number,
    MinTime : Number,
    isAvailable : Boolean,
    additionalCharges : Number,
    availability : {
        days: Array,
        slots: {
            from: Number , 
            to: Number ,
            fromFormat : String,
            toFormat: String
        }
    },
    imges:{
        thumbnail : String,
        large: String
    }
})
const Astro = mongoose.model("astros" , astroSchema) ;

const reportSchema = new mongoose.Schema({
    name: String ,
    thumbnailUrl: String,
    costPerMin: Number,
    detailUrl : String,
    description: String,
})
const Report = mongoose.model("reports" , reportSchema) ;

const questionsSchema = new mongoose.Schema({
    category: String ,
    categoryDesc: String,
    cost: Number ,
    suggestedQuestions:Array,
})
const Questions = mongoose.model("questions" , questionsSchema) ;

app.get("/" , async function(req ,res){
    const data_banner = await  Banner.find()
    const data_horoscope = await Horoscope.find()
    const data_astro = await Astro.find()
    const data_report = await Report.find()
    const data_questions = await Questions.find()

    res.send({
        "bannerOfferData" : data_banner,
        "horoscopeData" : data_horoscope,
        "astroData" : data_astro,
        "reportData" : data_report,
        "questionsData" : data_questions,
    }) 

})

app.listen(3000 , function(){
    console.log("Server is up and running") ;
})