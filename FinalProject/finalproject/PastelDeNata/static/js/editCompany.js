
function deleteImageField(anchor){
    anchor.parentNode.remove();
}

function addImageField(){
    const imageFieldContainer = document.getElementById("image-edit-container")
    var newElement = document.createElement("div");
    newElement.innerHTML = `<button class="inverse transparent-button" onclick="deleteImageField(this)">X</button><input type="text" name="companyPhoto" style="width:90%" placeholder="Hiperligacao...">`
    imageFieldContainer.appendChild(newElement)

}