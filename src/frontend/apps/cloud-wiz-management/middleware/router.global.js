export default defineNuxtRouteMiddleware((to, from) => {
   
    const  path = ['/auth/register','/auth/login'];
   
    
     if(path.includes('to.path') || useCookie('User').value ){
   
     }
     else{
         
          navigateTo('/auth/login')
    }
        
  })
  