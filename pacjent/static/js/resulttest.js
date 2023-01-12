

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
        if(info.value === "2"){
            leu.parentElement.style.display = 'block'
            erythrocytes.parentElement.style.display = 'none'
            hemoglobin.parentElement.style.display = 'none'
            hematocrit.parentElement.style.display = 'none'
            mcv.parentElement.style.display = 'none'
            mch.parentElement.style.display = 'none'
            mchc.parentElement.style.display = 'none'
            thrombocytes.parentElement.style.display = 'none'
            rdw.parentElement.style.display = 'none'
            pdw.parentElement.style.display = 'none'
            plcr.parentElement.style.display = 'none'
            neutrophils.parentElement.style.display = 'none'
        }else if(info.value === "1"){
            leu.parentElement.style.display = 'block'
            erythrocytes.parentElement.style.display = 'block'
            hemoglobin.parentElement.style.display = 'block'
            hematocrit.parentElement.style.display = 'block'
            mcv.parentElement.style.display = 'block'
            mch.parentElement.style.display = 'block'
            mchc.parentElement.style.display = 'block'
            thrombocytes.parentElement.style.display = 'block'
            rdw.parentElement.style.display = 'block'
            pdw.parentElement.style.display = 'block'
            plcr.parentElement.style.display = 'block'
            neutrophils.parentElement.style.display = 'block'
        }
    })
})


