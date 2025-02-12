// Drag & Drop Functionality
const dropArea = document.getElementById('drop-area');
const videoInput = document.getElementById('videoInput');

dropArea.addEventListener('click', () => videoInput.click());
dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.style.backgroundColor = '#d0e9ff';
});
dropArea.addEventListener('dragleave', () => {
    dropArea.style.backgroundColor = '#eaf4ff';
});
dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    videoInput.files = e.dataTransfer.files;
    dropArea.style.backgroundColor = '#eaf4ff';
});

// Tag System
let tags = [];
let charCount = 0;

const tagInput = document.getElementById('tagInput');
const addTagBtn = document.getElementById('addTagBtn');
const tagsDisplay = document.getElementById('tagsDisplay');
const charCountDisplay = document.getElementById('charCount');

addTagBtn.addEventListener('click', () => {
    const newTag = tagInput.value.trim().toLowerCase();

    if (newTag && newTag.length <= 90 && !tags.includes(newTag)) {
        const newCharCount = charCount + newTag.length;

        if (newCharCount <= 600) {
            tags.push(newTag);
            charCount = newCharCount;
            updateTags();
        } else {
            alert("Total character limit of 600 exceeded.");
        }
    }

    tagInput.value = '';
});

function updateTags() {
    tagsDisplay.innerHTML = '';
    tags.forEach(tag => {
        const tagElement = document.createElement('span');
        tagElement.classList.add('tag');
        tagElement.innerHTML = `${tag} <i class="fa fa-times" onclick="removeTag('${tag}')"></i>`;
        tagsDisplay.appendChild(tagElement);
    });
    charCountDisplay.textContent = `${charCount} / 600 characters used`;
}

function removeTag(tag) {
    tags = tags.filter(t => t !== tag);
    charCount -= tag.length;
    updateTags();
}

// Thumbnail Preview
document.getElementById('thumbnailInput').addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('thumbnailPreview').innerHTML = `<img src="${e.target.result}" alt="Thumbnail">`;
        };
        reader.readAsDataURL(file);
    }
});
