/* Repositorio de Publicaciones: filtros por categoría, buscador y visor PDF */
(function(){
  var grid=document.getElementById('pubGrid'); if(!grid) return;
  var cards=[].slice.call(grid.querySelectorAll('.pub'));
  var chips=[].slice.call(document.querySelectorAll('[data-pubfilter] .chip'));
  var search=document.getElementById('pubSearch');
  var empty=document.getElementById('pubEmpty');
  var cat='all', q='';
  function apply(){
    var n=0;
    cards.forEach(function(c){
      var okc = cat==='all' || c.getAttribute('data-cat')===cat;
      var okq = !q || (c.getAttribute('data-title')||'').indexOf(q)>-1;
      var show=okc&&okq; c.style.display=show?'':'none'; if(show)n++;
    });
    if(empty) empty.hidden = n>0;
  }
  chips.forEach(function(ch){ch.addEventListener('click',function(){
    chips.forEach(function(x){x.classList.remove('is-active');});
    ch.classList.add('is-active'); cat=ch.getAttribute('data-cat'); apply();
  });});
  if(search) search.addEventListener('input',function(){q=search.value.trim().toLowerCase();apply();});

  var m=document.createElement('div'); m.className='pdfm';
  m.innerHTML='<div class="pdfm__panel"><div class="pdfm__head"><b class="pdfm__t"></b><a class="pdfm__dl" download>Descargar</a><button class="pdfm__x" aria-label="Cerrar">&#10005;</button></div><iframe title="Visor de documento"></iframe></div>';
  document.body.appendChild(m);
  var fr=m.querySelector('iframe'), tt=m.querySelector('.pdfm__t'), dl=m.querySelector('.pdfm__dl');
  function openPdf(src,title){fr.src=src;tt.textContent=title||'Documento';dl.href=src;m.classList.add('is-open');document.body.style.overflow='hidden';}
  function closePdf(){m.classList.remove('is-open');fr.src='';document.body.style.overflow='';}
  grid.addEventListener('click',function(e){var b=e.target.closest('[data-pdf]');if(!b)return;openPdf(b.getAttribute('data-pdf'),b.getAttribute('data-title'));});
  m.addEventListener('click',function(e){if(e.target===m||e.target.closest('.pdfm__x'))closePdf();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')closePdf();});
})();
