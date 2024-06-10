<template>
<Breadcrumbs main="Dashboard" title="online" />
<div class="container-fluid">
    <div class="row">
        <welcomeCard />
        <todayProgressCard />
        <doyouWanttoGetCard />
        <datePickerCard />
        <learningOverviewCard />
        <activityHoursCard />
        <upcomingEventsCard />
        <myCourseCardVue />
        <upcomingScheduleCard />
        <activeLessonsCard />
    </div>
</div>
</template>

<script>
import welcomeCard from './welcomeCard.vue'
import todayProgressCard from './todayProgressCard.vue'
import doyouWanttoGetCard from './doyouWanttoGetCard.vue'
import datePickerCard from './datePickerCard.vue'
import learningOverviewCard from './learningOverviewCard.vue'
import activityHoursCard from './activityHoursCard.vue'
import upcomingEventsCard from './upcomingEventsCard.vue'
import myCourseCardVue from './myCourseCard.vue'
import upcomingScheduleCard from './upcomingScheduleCard.vue'
import activeLessonsCard from './activeLessonsCard.vue'

export default {
    components: {
        welcomeCard,
        todayProgressCard,
        doyouWanttoGetCard,
        datePickerCard,
        learningOverviewCard,
        activityHoursCard,
        upcomingEventsCard,
        myCourseCardVue,
        upcomingScheduleCard,
        activeLessonsCard

    },
    data() {
        return {

        }
    }
}
</script>
