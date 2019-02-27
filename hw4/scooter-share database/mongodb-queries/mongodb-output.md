##1 Read all scooters that have a max speed of 25.
```
db.scooters.find({ max_speed:25 })

{ "_id" : ObjectId("5c0d9075f1e97d739b344a36"), "acquired_date" : "2018-01-08", "retired" : true, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a39"), "acquired_date" : "2015-04-27", "retired" : true, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a3a"), "acquired_date" : "2014-01-10", "retired" : false, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a3b"), "acquired_date" : "2016-05-06", "retired" : true, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a3c"), "acquired_date" : "2015-04-25", "retired" : true, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a3e"), "acquired_date" : "2015-04-25", "retired" : false, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a3f"), "acquired_date" : "2016-12-22", "retired" : false, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a40"), "acquired_date" : "2016-08-07", "retired" : false, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a41"), "acquired_date" : "2015-01-25", "retired" : false, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a42"), "acquired_date" : "2015-12-07", "retired" : true, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a44"), "acquired_date" : "2016-09-16", "retired" : true, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a46"), "acquired_date" : "2015-09-16", "retired" : true, "scooter_type" : "model9", "max_speed" : 25, "weight" : 27, "company" : "company0", "website" : "company0.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a57"), "acquired_date" : "2017-09-01", "retired" : true, "scooter_type" : "model3", "max_speed" : 25, "weight" : 26, "company" : "company2", "website" : "company2.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a5b"), "acquired_date" : "2016-12-22", "retired" : false, "scooter_type" : "model3", "max_speed" : 25, "weight" : 26, "company" : "company2", "website" : "company2.com" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a5c"), "acquired_date" : "2016-03-18", "retired" : false, "scooter_type" : "model3", "max_speed" : 25, "weight" : 26, "company" : "company2", "website" : "company2.com" }
```

##2 Read the scooter type and company for the first 10 scooters. 
```
db.scooters.find({}, { scooter_type:1, company:1 }).limit(10)

{ "_id" : ObjectId("5c0d9075f1e97d739b3449ed"), "scooter_type" : "model4", "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449ee"), "scooter_type" : "model6", "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449ef"), "scooter_type" : "model4", "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f0"), "scooter_type" : "model4", "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f1"), "scooter_type" : "model8", "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f2"), "scooter_type" : "model8", "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f3"), "scooter_type" : "model4", "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f4"), "scooter_type" : "model8", "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f5"), "scooter_type" : "model8", "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f6"), "scooter_type" : "model8", "company" : "company3" }
```

##3 Read all scooters from company0 that are not retired.
```
db.scooters.find({ retired:true, company:"company0" }, { scooter_type:1, _id:0 })

{ "scooter_type" : "model3" }
{ "scooter_type" : "model7" }
{ "scooter_type" : "model7" }
{ "scooter_type" : "model8" }
{ "scooter_type" : "model8" }
{ "scooter_type" : "model8" }
{ "scooter_type" : "model8" }
{ "scooter_type" : "model9" }
{ "scooter_type" : "model9" }
{ "scooter_type" : "model9" }
{ "scooter_type" : "model9" }
{ "scooter_type" : "model8" }
{ "scooter_type" : "model8" }
{ "scooter_type" : "model8" }
{ "scooter_type" : "model9" }
{ "scooter_type" : "model8" }
{ "scooter_type" : "model9" }
{ "scooter_type" : "model9" }
{ "scooter_type" : "model9" }
{ "scooter_type" : "model9" }
{ "scooter_type" : "model9" }
{ "scooter_type" : "model9" }
{ "scooter_type" : "model3" }
{ "scooter_type" : "model3" }
```

##4 Read all scooters that have a weight greater than 28.
```
db.scooters.find({ weight:{$gt:28} }, { company:1, scooter_type:1, weight: 1 })

{ "_id" : ObjectId("5c0d9075f1e97d739b3449f1"), "scooter_type" : "model8", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f2"), "scooter_type" : "model8", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f4"), "scooter_type" : "model8", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f5"), "scooter_type" : "model8", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f6"), "scooter_type" : "model8", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f7"), "scooter_type" : "model8", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f8"), "scooter_type" : "model8", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449f9"), "scooter_type" : "model9", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449fa"), "scooter_type" : "model9", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449fb"), "scooter_type" : "model8", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449fc"), "scooter_type" : "model9", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449fd"), "scooter_type" : "model9", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449fe"), "scooter_type" : "model9", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b3449ff"), "scooter_type" : "model9", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a00"), "scooter_type" : "model9", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a01"), "scooter_type" : "model9", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a02"), "scooter_type" : "model9", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a03"), "scooter_type" : "model9", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a06"), "scooter_type" : "model9", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a0c"), "scooter_type" : "model8", "weight" : 30, "company" : "company3" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a1f"), "scooter_type" : "model3", "weight" : 29, "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a4b"), "scooter_type" : "model3", "weight" : 29, "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a4c"), "scooter_type" : "model3", "weight" : 29, "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a4d"), "scooter_type" : "model3", "weight" : 29, "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a4e"), "scooter_type" : "model7", "weight" : 30, "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a4f"), "scooter_type" : "model7", "weight" : 30, "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a50"), "scooter_type" : "model7", "weight" : 30, "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a51"), "scooter_type" : "model7", "weight" : 30, "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a52"), "scooter_type" : "model7", "weight" : 30, "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a58"), "scooter_type" : "model7", "weight" : 30, "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a59"), "scooter_type" : "model7", "weight" : 30, "company" : "company1" }
```

##5 Read all scooters that are from company0 or company1. 
```
db.scooters.find({ $or : [{company:"company0"}, {company:"company1"}] }, { company:1 })

{ "_id" : ObjectId("5c0d9075f1e97d739b344a1e"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a1f"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a20"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a21"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a22"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a23"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a24"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a25"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a26"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a27"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a28"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a29"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a2a"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a2b"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a2c"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a2d"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a2e"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a2f"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a30"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a31"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a32"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a33"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a34"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a35"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a36"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a37"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a38"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a39"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a3a"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a3b"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a3c"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a3d"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a3e"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a3f"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a40"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a41"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a42"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a43"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a44"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a45"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a46"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a47"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a48"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a49"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a4a"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a4b"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a4c"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a4d"), "company" : "company0" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a4e"), "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a4f"), "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a50"), "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a51"), "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a52"), "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a53"), "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a54"), "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a55"), "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a56"), "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a58"), "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a59"), "company" : "company1" }
{ "_id" : ObjectId("5c0d9075f1e97d739b344a5a"), "company" : "company1" }
```
