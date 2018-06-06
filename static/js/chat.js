var Message;
Message = function (arg)
{
 this.text = arg.text, this.messageside = arg.messageside;
 this.draw = function (_this)
  {
   return function ()
   {
     var $message;
     $message = $($('.messagetemplate').clone().html());
     $message.addClass(_this.messageside).find('.text').html(addBreak(_this.text));
     $('.messages').append($message);
     return setTimeout(function ()
     {
      return $message.addClass('appeared');
     }, 0);
   };
  }(this);
  return this;
};

/*Following function will add breaks at the end of each text globally*/
function addBreak(text)
{
 return text.replace(/\n/g, "<br />");
}

/*Following function will setup bot message properties, and specifies the left direction from where it will float on to the
chat panel*/
function botMsgProp(msg)
{
   message = new Message({
             text: msg,
             messageside: 'left'
   });
   message.draw();
   $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 100);
}

/*Following function will setup user message properties, and specifies the right direction from where it will float on to the
chat panel*/
function userMsgProp(msg)
{
   $messages = $('.messages');
   message = new Message({
             text: msg,
             messageside: 'right'
   });
   message.draw();
   $messages.animate({scrollTop: $messages.prop('scrollHeight')}, 100);
   $('#input').val('');
}

function botMsgs(text)
{
 document.getElementById("input").placeholder = "Type your message here..."
 $.post("/chat",
 {
  text:text,
 },
 function(jsondata, status)
 {
  if(jsondata["status"]=="success")
  {
   response=jsondata["response"];
   if(response){botMsgProp(response);}
  }
 });
}

/*when user clicks send button, the user message should go to chat window and bot message should come in chat window*/
$('.sendbutton').click(function (e) {
        msg = getMsgTxt();
        if(msg){
        userMsgProp(msg);
        botMsgs(msg);
    $('.msginput').val('');}
});

/*when user hits enter, the user message should go to chat window and bot message should come in chat window*/
$('.msginput').keyup(function (e)
{
    if (e.which === 13) {
        msg = getMsgTxt();
        if(msg){
        userMsgProp(msg);
        botMsgs(msg);
    $('.msginput').val('') ;}
    }
});

/*following function when called returns value of the input message*/
getMsgTxt = function ()
{
  var $msginput;
  $msginput = $('.msginput');
  return $msginput.val();
};


