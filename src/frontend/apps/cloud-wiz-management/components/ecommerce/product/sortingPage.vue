<template>
    <div class="col-md-6 text-sm-end"><span class="f-w-600 m-r-5">Showing Products 1 - 24 Of 200 Results</span>
        <div class="select2-drpdwn-product select-options d-inline-block ms-1">
            <select class="form-control btn-square" @change="onChangeSort($event)" name="select">
                <option value="a-z">Featured</option>
                <option value="low">Lowest Prices</option>
                <option value="high">Highest Prices</option>
            </select>
        </div>
    </div>
</template>
<script>
import { useProductStore } from '~~/store/product'
export default {
    name: 'sortingPage',
    methods: {
        onChangeSort(event) {
            useProductStore().sortProducts(event.target.value)
        },
    }
}
</script>