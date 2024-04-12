
function deleteImageField(anchor){
    anchor.parentNode.remove();
}

function uploadImage(){
    const uploadInput = document.getElementById('upload-image-company');
    const imageContainer = document.getElementById('company-card-images');

    const file = uploadInput.files[0];

    if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();

        reader.onload = function(event) {
            const imageUrl = event.target.result;
                const img = document.createElement('img');
                const remove_btn = document.createElement('button');
                img.src = imageUrl;
                img.setAttribute("name", "companyPhoto")
                const div = document.createElement('div');
                remove_btn.classList.add('remove-picture-button');
                remove_btn.setAttribute("onclick", "deleteImageField(this)")
                remove_btn.type = "button"
                div.appendChild(img);
                div.appendChild(remove_btn);
                imageContainer.insertBefore(div, uploadInput);

                var hiddenInput = uploadInput.cloneNode(true)
                hiddenInput.setAttribute('name', 'companyPhotosSrc');
                hiddenInput.setAttribute('style', 'display:none');
                hiddenInput.setAttribute('id', 'upload-image-company-secondary');
                div.appendChild(hiddenInput);
        }
        reader.readAsDataURL(file);
    } else {
        alert('Please upload an image file.');
    }
}
function addImageField(){
    const imageFieldContainer = document.getElementById("image-edit-container")
    var newElement = document.createElement("div");
    newElement.innerHTML = `<button class="inverse transparent-button" onclick="deleteImageField(this)">X</button><input type="text" name="companyPhoto" style="width:90%" placeholder="Hiperligacao...">`
    imageFieldContainer.appendChild(newElement)

}
