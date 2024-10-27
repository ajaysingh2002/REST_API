async function fetchImages() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/images/');
        const images = await response.json();
        const gallery = document.getElementById('api');
        
        images.forEach(image => {
          
            const galleryItem = document.createElement('div');
            galleryItem.className = 'gallery-item';

            const img = document.createElement('img');
            img.src = image.image;  
            img.alt = image.description;

            const title = document.createElement('h1');
            title.textContent = image.title;
            
            const desc = document.createElement('p');
            desc.textContent = image.description;

            galleryItem.appendChild(img);
            galleryItem.appendChild(title);
            galleryItem.appendChild(desc);

         
            gallery.appendChild(galleryItem);
        });
    } catch (error) {
        console.error('Error fetching images:', error);
    }
}


document.addEventListener('DOMContentLoaded', fetchImages);
