/* Lightbox de galería (visor de imágenes con navegación) */
(function(){
  var cells=[].slice.call(document.querySelectorAll('.gcell')); if(!cells.length) return;
  var lb=document.createElement('div'); lb.className='lb';
  lb.innerHTML='<button class="lb__x" aria-label="Cerrar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg></button>'+
    '<button class="lb__nav prev" aria-label="Anterior"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 18-6-6 6-6"/></svg></button>'+
    '<img alt="">'+
    '<button class="lb__nav next" aria-label="Siguiente"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 6 6 6-6 6"/></svg></button>'+
    '<div class="lb__cap"></div>';
  document.body.appendChild(lb);
  var im=lb.querySelector('img'), cap=lb.querySelector('.lb__cap'), i=0;
  function show(n){i=(n+cells.length)%cells.length;var c=cells[i];im.src=c.getAttribute('data-full');cap.textContent=c.getAttribute('data-cap')||'';}
  function open(n){show(n);lb.classList.add('is-open');document.body.style.overflow='hidden';}
  function close(){lb.classList.remove('is-open');document.body.style.overflow='';}
  cells.forEach(function(c,n){c.addEventListener('click',function(){open(n);});});
  lb.querySelector('.lb__x').addEventListener('click',close);
  lb.querySelector('.prev').addEventListener('click',function(e){e.stopPropagation();show(i-1);});
  lb.querySelector('.next').addEventListener('click',function(e){e.stopPropagation();show(i+1);});
  lb.addEventListener('click',function(e){if(e.target===lb)close();});
  document.addEventListener('keydown',function(e){if(!lb.classList.contains('is-open'))return;if(e.key==='Escape')close();if(e.key==='ArrowLeft')show(i-1);if(e.key==='ArrowRight')show(i+1);});
})();
