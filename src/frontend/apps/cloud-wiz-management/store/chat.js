import users from '@/data/chatmember.json';
import { defineStore } from 'pinia';
export const useChatStore = defineStore({
    id:'chat',
    state:()=>{
        return{
            all: users.data,
            users: users.data,
            serchUser: users.data,
            chats: users.chat,
            activeuser:1,
        }
    },
    getters:{
        currentChat: (state) => {
            var chats = state.chats.find( chat => {
                if(chat.id === state.activeuser)
                    return chat;
            });
            var users = state.users.find( user => {
                if(user.id === state.activeuser)
                    return user;
            });
            return { ...users,'chat':chats };
        },
    },
    actions:{
        addChat ( payload)  {
            var today = new Date().toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
            const id = this.activeuser;
            const addchat = this.chats.find(chat => chat.id === id);
            addchat.messages.push({ 'sender': 0, 'time': today.toLowerCase(), 'text': payload });
        setTimeout(function () {
            useChatStore().addChatResponce()
        },1000);
    
    },
    addChatResponce(){
        var today = new Date().toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
        const id = this.activeuser;
        const addchat = this.chats.find(chat => chat.id === id);
        addchat.messages.push({ 'sender': id , 'time': today.toLowerCase(), 'text': '... I will text you later.' });
    },
    setActiveuser(payload)  {

        this.activeuser = payload;

        const chats = this.chats.find( chat => {
            if(chat.id === payload)
                return chat;
        });
        if(!chats) {
            this.users.find( user => {
                if(user.id === payload) {
                    user.active = 'active';
                }
            });
            this.chats.push({
                'id': payload,
                'users': [
                    0,
                    payload
                ],
                'lastMessageTime': 'Last seen yesterday 14:14',
                'messages': [],
                "video":[]
            });
        }
    },
     setSerchUsers(payload) {
        this.serchUser = this.all.filter(function (search) {
            if (search.name.toLowerCase().search(payload.toLowerCase()) !== -1 && search.id !== 0)
                return search;
        });
    }
}
})
