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

info.addEventListener('click', () => {
    info.addEventListener('change', () => {

        //leukocytes
        if(info.value === "1" || info.value === "2"){
            leu.parentElement.style.display = 'block'
        }else{
            leu.parentElement.style.display = 'none'
        }

        //erythrocytes
        if(info.value === "1"){
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
    })
})


