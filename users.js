db.user.insert({_id_user:1, first_name:"José Miguel", last_name:"Medina Valero", email:"jsmiguel1702@gmail.com", password:"pbkdf2:sha256:50000$PYIaIhQI$40e3547853d432443394fa54d3e049efb73e1d628e19ab06a64271e28d523bcd", birthdate:"17/02/95", facebook:"https://www.facebook.com/josemiguel.medinavalero", twitter:"https://twitter.com/Jos_MMV", images:[{_id_image:1}, {_id_image:2}, {_id_image:3}, {_id_image:8}], profile_image:"../static/img/img9.jpg", friendships:[{_id_user:2}, {_id_user:3}], conf: true})
db.user.insert({_id_user:2, first_name:"Juan", last_name:"Figueira", email:"juanfigueira@gmail.com", password:"pbkdf2:sha256:50000$HlQQk52W$8639653bd1dbc0fcd9f7f89a6ccab9b854c09b1f5f4b2bb9873c8dc8d76007f1", birthdate:"13/01/94", images:[{_id_image:4}], profile_image:"../static/img/img10.jpg", friendships:[{_id_user:1}], conf: true})
db.user.insert({_id_user:3, first_name:"Kevin", last_name:"Blanco", email:"kevinblanco@gmail.com", password:"pbkdf2:sha256:50000$r5FizWCH$18c5392eec90f7d9b4a8e4c29ef7c1ffbe319ad4fe84d7602b1e62de875dbf43", birthdate:"16/09/94", images:[{_id_image:7}, {_id_image:5}, {_id_image:6}], profile_image:"../static/img/img11.png", friendships:[{_id_user:1}], conf: false})
/*contraseñas:
jsmiguel1702@gmail.com 12344321
juanfigueira@gmail.com qwerty
kevinblanco@gmail.com universidadcentral123
*/
db.image.insert({_id_image:1, src:"../static/img/img1.jpg", tittle:"Primera imagen de José", date:"13/01/18", description:"Descripción 1 de José", likes:[{_id_user:2, calif:3}, {_id_user:3, calif:4}], comments:[{_id_user:2, comment:"Nawebonada vladi1000"}], conf: false})
db.image.insert({_id_image:2, src:"../static/img/img2.jpg", tittle:"Segunda imagen de José", date:"14/01/18", description:"Descripción 2 de José", likes:[{_id_user:3, calif:4}], comments:[{_id_user:2, comment:"Esto es un comentario del usuario 2"}], conf: false})
db.image.insert({_id_image:3, src:"../static/img/img3.jpg", tittle:"Tercera imagen de José", date:"17/02/18", description:"Descripción 3 de José", likes:[{_id_user:2, calif:5}], comments:[{_id_user:3, comment:"Esto es otro comentario equis"}], conf: true})
db.image.insert({_id_image:4, src:"../static/img/img4.jpg", tittle:"Primera imagen de Juan", date:"02/02/18", description:"Descripción 1 de Juan", likes:[{_id_user:1, calif:4},{_id_user:3, calif:4}], comments:[{_id_user:3, comment:"Cualquier vaina"}], conf: false})
db.image.insert({_id_image:5, src:"../static/img/img5.jpg", tittle:"Primera imagen de Kevin", date:"04/02/18", description:"Descripción 1 de Kevin", likes:[{_id_user:2, calif:2}], comments:[{_id_user:2, comment:"Baia baia"}], conf: false})
db.image.insert({_id_image:6, src:"../static/img/img6.jpg", tittle:"Segunda imagen de Kevin", date:"04/02/18", description:"Descripción 2 de Kevin", likes:[{_id_user:2, calif:1}], comments:[{_id_user:2, comment:"Un comentario cualquiera"}], conf: true})
db.image.insert({_id_image:7, src:"../static/img/img7.jpg", tittle:"Tercera imagen de Kevin", date:"14/03/18", description:"Descripción 3 de Kevin", likes:[{_id_user:1, calif:3}], comments:[{_id_user:1, comment:"Otro comentario cualquiera"}], conf: true})
db.image.insert({_id_image:8, src:"../static/img/img8.jpg", tittle:"Cuarta imagen de José", date:"23/04/18", description:"Descripción 4 de José", likes:[{_id_user:3, calif:4}], comments:[], conf: true})

/*db.users.insert({_id_user:, first_name:"", last_name:"", email:"",password:"",  birthdate:"", facebook:"", twitter:"", images:[{id_image:}, {id_image:}, {id_image:}], profile_image:"../static/img/img10.jpg", friendships:[{_id_user:}, {_id_user:}]})
db.image.insert({_id_image:, src:"../static/img/img.jpg",  tittle:"", date:"", description:"", likes:[{_id_user:, calif:}], comments:[{_id_user:, comment:""}, conf: true]})
*/