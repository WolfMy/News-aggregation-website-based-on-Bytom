 var fade = ['scale(0,0)', 'scale(1,1)'];
 var cnt = [0, 0, 0, 0, 0, 0],
     number = [-1, -1, -1, -1, -1, -1];

 function refreshTime() {
     var timeNow = new Date().toTimeString().substring(0, 8).replace(':', '').replace(':', '');
     var els = document.getElementsByClassName('timeNum');
     for (var i = 0; i < els.length; i++) {
         if (timeNow[i] == number[i]) continue;
         var el = els[i];
         cnt[i] = (cnt[i] + 1) % 2;
         if (cnt[i] != 0) {
             el.innerText = timeNow[i];
             number[i] = timeNow[i];
             el.style.transitionDelay = '0s';
         } else el.style.transitionDelay = '0.2s';
         el.style.transform = fade[cnt[i]];
     }
 };