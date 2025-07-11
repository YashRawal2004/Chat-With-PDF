
css = '''
<style>
body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #1e1e2f;
    color: #ffffff;
}

.chat-message {
    padding: 1.25rem;
    border-radius: 1rem;
    margin: 1rem 0;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.3);
}

.chat-message.user {
    background: linear-gradient(135deg, #2b313e, #3d4455);
    border-left: 5px solid #56ccf2;
}

.chat-message.bot {
    background: linear-gradient(135deg, #475063, #586179);
    border-left: 5px solid #bb6bd9;
}

.chat-message .avatar {
    flex-shrink: 0;
}

.chat-message .avatar img {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #fff;
}

.chat-message .message {
    flex-grow: 1;
    font-size: 1rem;
    line-height: 1.6;
    color: #f0f0f0;
    word-wrap: break-word;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://thumbs.dreamstime.com/b/happy-man-character-rejoicing-cheering-vector-illustration-young-elated-male-feeling-excitement-concept-295858619.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
