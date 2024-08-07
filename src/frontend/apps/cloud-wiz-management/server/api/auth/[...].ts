import GoogleProvider from "next-auth/providers/google";
import { NuxtAuthHandler } from '#auth'

export default NuxtAuthHandler({
    secret: 'UEZ9i4EMsk',
    providers: [
        GoogleProvider.default({
            clientId: '990032385398-1irlaingq367jd5rc2dg1pd4fsga0dnn.apps.googleusercontent.com',
            clientSecret: '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',
            authorization: {
                params: {
                    scope: "openid profile email https://www.googleapis.com/auth/drive",
                    prompt: "consent",
                    access_type: "offline",
                    response_type: "code"
                }
            }
        })
    ],
    callbacks: {
        /* on before signin */
        async signIn({ user, account, profile, email, credentials }) {
            const isAllowedToSignIn = true
            if (isAllowedToSignIn) {
                return true
            } else {
                return false
            }
        },
        /* on redirect to another url */
        async redirect({ url, baseUrl }) {
            return '/google/callback';
        },
        /* on session retrival */
        async session({ session, user, token }) {
            return session
        },
        /* on JWT token creation or mutation */
        async jwt({ token, user, account, profile, isNewUser }) { 
            if (account) {
                token.access_token = account.access_token
                token.refresh_token = account.refresh_token
            }
            return token
        }     
    }  
})