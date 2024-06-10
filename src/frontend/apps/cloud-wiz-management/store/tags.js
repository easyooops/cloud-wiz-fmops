import tags from '@/data/tags.json'
export const useTagStore = defineStore({
	id: 'Tags',
	state:()=>{
		return{
			tags: tags.data,
			activeclass1 : 'pills-created-tab'
		}
	},
	getters:{
		activeclass:(state)=>{ return state.activeclass1}
},
actions:{
	add(payload){
		this.tags.push(payload);
		
	},
    active(payload){
		this.activeclass1 = payload
	},
}
})
