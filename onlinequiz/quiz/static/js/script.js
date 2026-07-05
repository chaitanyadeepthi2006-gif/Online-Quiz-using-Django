
// Confirm before submitting quiz
function confirmSubmit(){

    let result = confirm("Are you sure you want to submit the quiz?");

    if(result){
        return true;
    }
    else{
        return false;
    }
}