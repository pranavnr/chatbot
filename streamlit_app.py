components.html("""
<div id= "chatbot">
<script>
!function(w, d, s, ...args){
  var div = d.createElement('div');
  div.id = 'aichatbot';
  d.body.appendChild(div);
  w.chatbotConfig = args;

  var f = d.getElementsByTagName(s)[0],
  j = d.createElement(s);
  j.defer = true;
  j.type = 'module';
  j.src = 'https://aichatbot.sendbird.com/index.js';
  f.parentNode.insertBefore(j, f);
}(window, document, 'script', 'C693D7FF-6D67-4E97-9D6F-62330391FC91', 'onboarding_bot');
</script>
</div>
""")
