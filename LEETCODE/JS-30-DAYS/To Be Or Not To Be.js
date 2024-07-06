let expect = (val) =>{

    return {
        toBe : (paramTOBE)=>{
        if(paramTOBE === val){return true ;} 
        throw new Error("Not Equal") ;
        },

        notToBe :(paramNOT_TO_BE) =>{
        if(paramNOT_TO_BE !== val){return true ;}
        throw new Error("Equal") ;
        }

    } ;

} ;
