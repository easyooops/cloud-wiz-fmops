import { getToken } from '#auth'

export default eventHandler((event: any) => getToken({ event }))