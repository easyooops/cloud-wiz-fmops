import Jobs from "@/data/jobs.json"
export const useJobStore = defineStore({
	id: 'job',
	state:()=>{
		return{

			jobs : Jobs.jobs
		}

	}
})
