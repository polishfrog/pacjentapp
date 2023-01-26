let info = document.querySelector('#id_test')
let leu = document.querySelector('#id_leukocytes')
let erythrocytes = document.querySelector('#id_erythrocytes')
let hemoglobin = document.querySelector('#id_hemoglobin')
let hematocrit = document.querySelector('#id_hematocrit')
let mcv = document.querySelector('#id_mcv')
let mch = document.querySelector('#id_mch')
let mchc = document.querySelector('#id_mchc')
let thrombocytes = document.querySelector('#id_thrombocytes')
let rdw = document.querySelector('#id_rdw')
let pdw = document.querySelector('#id_pdw')
let plcr = document.querySelector('#id_plcr')
let neutrophils = document.querySelector('#id_neutrophils')
let volume = document.querySelector('#id_volume')
let specific_gravity = document.querySelector('#id_specific_gravity')
let color = document.querySelector('#id_color')
let smell = document.querySelector('#id_smell')
let look = document.querySelector('#id_look')
let ph = document.querySelector('#id_ph')
let glucose = document.querySelector('#id_glucose')
let protein = document.querySelector('#id_protein')
let nitrites = document.querySelector('#id_nitrites')
let ketone_bodies = document.querySelector('#id_ketone_bodies')
let bilirubin = document.querySelector('#id_bilirubin')
let urobilinogen = document.querySelector('#id_urobilinogen')
let glassy_rods = document.querySelector('#id_glassy_rods')
let epithelial_rollers = document.querySelector('#id_epithelial_rollers')
let erythrocytes_casts = document.querySelector('#id_erythrocytes_casts')
let leukocyte_casts = document.querySelector('#id_leukocyte_casts')
let grain_rolls = document.querySelector('#id_grain_rolls')
let flat_epithelium = document.querySelector('#id_flat_epithelium')
let round_epithelium = document.querySelector('#id_round_epithelium')
let bacteria = document.querySelector('#id_bacteria')
let yeast = document.querySelector('#id_yeast')
let oxalates = document.querySelector('#id_oxalates')
let soaked = document.querySelector('#id_soaked')
let phosphates = document.querySelector('#id_phosphates')


leu.parentElement.style.display = 'none'
mch.parentElement.style.display = 'none'
erythrocytes.parentElement.style.display = 'none'
hemoglobin.parentElement.style.display = 'none'
hematocrit.parentElement.style.display = 'none'
mcv.parentElement.style.display = 'none'
mchc.parentElement.style.display = 'none'
thrombocytes.parentElement.style.display = 'none'
rdw.parentElement.style.display = 'none'
pdw.parentElement.style.display = 'none'
plcr.parentElement.style.display = 'none'
neutrophils.parentElement.style.display = 'none'
volume.parentElement.style.display = 'none'
specific_gravity.parentElement.style.display = 'none'
color.parentElement.style.display = 'none'
smell.parentElement.style.display = 'none'
look.parentElement.style.display = 'none'
ph.parentElement.style.display = 'none'
glucose.parentElement.style.display = 'none'
protein.parentElement.style.display = 'none'
nitrites.parentElement.style.display = 'none'
ketone_bodies.parentElement.style.display = 'none'
bilirubin.parentElement.style.display = 'none'
glassy_rods.parentElement.style.display = 'none'
urobilinogen.parentElement.style.display = 'none'
epithelial_rollers.parentElement.style.display = 'none'
erythrocytes_casts.parentElement.style.display = 'none'
leukocyte_casts.parentElement.style.display = 'none'
grain_rolls.parentElement.style.display = 'none'
flat_epithelium.parentElement.style.display = 'none'
round_epithelium.parentElement.style.display = 'none'
bacteria.parentElement.style.display = 'none'
yeast.parentElement.style.display = 'none'
oxalates.parentElement.style.display = 'none'
soaked.parentElement.style.display = 'none'
phosphates.parentElement.style.display = 'none'


info.addEventListener('click', () => {
    info.addEventListener('change', () => {

        //leukocytes
        if(info.value === "1" || info.value === "2"){
            leu.parentElement.style.display = 'block'
        }else{
            leu.parentElement.style.display = 'none'
        }

        //erythrocytes
        if(info.value === "1" || info.value === "2"){
            erythrocytes.parentElement.style.display = 'block'
        }else{
            erythrocytes.parentElement.style.display = 'none'
        }

        //hemoglobin
        if(info.value === "1"){
            hemoglobin.parentElement.style.display = 'block'
        }else{
            hemoglobin.parentElement.style.display = 'none'
        }

        //hematocrit
        if(info.value === "1"){
            hematocrit.parentElement.style.display = 'block'
        }else{
            hematocrit.parentElement.style.display = 'none'
        }

        //mcv
        if(info.value === "1"){
            mcv.parentElement.style.display = 'block'
        }else{
            mcv.parentElement.style.display = 'none'
        }

        //mch
        if(info.value === "1"){
            mch.parentElement.style.display = 'block'
        }else{
            mch.parentElement.style.display = 'none'
        }

        //mchc
        if(info.value === "1"){
            mchc.parentElement.style.display = 'block'
        }else{
            mchc.parentElement.style.display = 'none'
        }

        //thrombocytes
        if(info.value === "1"){
            thrombocytes.parentElement.style.display = 'block'
        }else{
            thrombocytes.parentElement.style.display = 'none'
        }

        //rdw
        if(info.value === "1"){
            rdw.parentElement.style.display = 'block'
        }else{
            rdw.parentElement.style.display = 'none'
        }

        //pdw
        if(info.value === "1"){
            pdw.parentElement.style.display = 'block'
        }else{
            pdw.parentElement.style.display = 'none'
        }

        //plcr
        if(info.value === "1"){
            plcr.parentElement.style.display = 'block'
        }else{
            plcr.parentElement.style.display = 'none'
        }

        //plcr
        if(info.value === "1"){
            neutrophils.parentElement.style.display = 'block'

        }else{
            neutrophils.parentElement.style.display = 'none'
        }

        //volume
        if(info.value === "2"){
            volume.parentElement.style.display = 'block'
        }else {
            volume.parentElement.style.display = 'none'
        }

        //specific_gravity
        if(info.value === "2"){
            specific_gravity.parentElement.style.display = 'block'
        }else{
            specific_gravity.parentElement.style.display = 'none'
        }

        //color
        if(info.value === "2"){
            color.parentElement.style.display = 'block'
        }else{
            color.parentElement.style.display = 'none'
        }

        //smell
        if(info.value === "2"){
            smell.parentElement.style.display = 'block'
        }else{
            smell.parentElement.style.display = 'none'
        }

        //look
        if(info.value === "2"){
            look.parentElement.style.display = 'block'
        }else{
            look.parentElement.style.display = 'none'
        }

        //ph
        if(info.value === "2"){
            ph.parentElement.style.display = 'block'
        }else{
            ph.parentElement.style.display = 'none'
        }

        //glucose
        if(info.value === "2"){
            glucose.parentElement.style.display = 'block'
        }else{
            glucose.parentElement.style.display = 'none'
        }

        //protein
        if(info.value === "2"){
            protein.parentElement.style.display = 'block'
        }else{
            protein.parentElement.style.display = 'none'
        }

        //nitrites
        if(info.value === "2"){
            nitrites.parentElement.style.display = 'block'
        }else{
            nitrites.parentElement.style.display = 'none'
        }

        //ketone_bodies
        if(info.value === "2"){
            ketone_bodies.parentElement.style.display = 'block'
        }else{
            ketone_bodies.parentElement.style.display = 'none'
        }

        //bilirubina
        if(info.value === "2"){
            bilirubin.parentElement.style.display = 'block'
        }else{
            bilirubin.parentElement.style.display = 'none'
        }

        //urobilinogen
        if(info.value === "2"){
            urobilinogen.parentElement.style.display = 'block'
        }else{
            urobilinogen.parentElement.style.display = 'none'
        }

        //glassy_rods
        if(info.value === "2"){
            glassy_rods.parentElement.style.display = 'block'
        }else{
            glassy_rods.parentElement.style.display = 'none'
        }

        //epithelial_rollers
        if(info.value === "2"){
            epithelial_rollers.parentElement.style.display = 'block'
        }else{
            epithelial_rollers.parentElement.style.display = 'none'
        }

        //erythrocytes_casts
        if(info.value === "2"){
            erythrocytes_casts.parentElement.style.display = 'block'
        }else{
            erythrocytes_casts.parentElement.style.display = 'none'
        }

        //leukocyte_casts
        if(info.value === "2"){
            leukocyte_casts.parentElement.style.display = 'block'
        }else{
            leukocyte_casts.parentElement.style.display = 'none'
        }

        //flat_epithelium
        if(info.value === "2"){
            flat_epithelium.parentElement.style.display = 'block'
        }else{
            flat_epithelium.parentElement.style.display = 'none'
        }

        //grain_rolls
        if(info.value === "2"){
            grain_rolls.parentElement.style.display = 'block'
        }else{
            grain_rolls.parentElement.style.display = 'none'
        }

        //round_epithelium
        if(info.value === "2"){
            round_epithelium.parentElement.style.display = 'block'
        }else{
            round_epithelium.parentElement.style.display = 'none'
        }

        //bacteria
        if(info.value === "2"){
            bacteria.parentElement.style.display = 'block'
        }else{
            bacteria.parentElement.style.display = 'none'
        }

        //yeast
        if(info.value === "2"){
            yeast.parentElement.style.display = 'block'
        }else{
            yeast.parentElement.style.display = 'none'
        }

        //oxalates
        if(info.value === "2"){
            oxalates.parentElement.style.display = 'block'
        }else{
            oxalates.parentElement.style.display = 'none'
        }

        //soaked
        if(info.value === "2"){
            soaked.parentElement.style.display = 'block'
        }else{
            soaked.parentElement.style.display = 'none'
        }

        //phosphates
        if(info.value === "2"){
            phosphates.parentElement.style.display = 'block'
        }else{
            phosphates.parentElement.style.display = 'none'
        }
    })
})


