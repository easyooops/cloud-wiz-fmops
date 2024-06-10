<template>
    <breadCrumbs title="Hide Menu On Scroll" main="Page Layout" title1="Hide Menu On Scroll" />

    <div class="container-fluid">
        <div class="row">
            <div class="col-sm-12">
                <div class="card">
                    <div class="card-header">
                        <h3>Sample Card</h3><span>lorem ipsum dolor sit amet, consectetur adipisicing elit</span>
                    </div>
                    <div class="card-body">
                        <p v-for="(item, index) in 4" :key="index">
                            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                            enim ad minim veniam, quis nostrud exercitation ullamco laboris
                            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                            in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                            nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                            sunt in culpa qui officia deserunt mollit anim id est laborum.
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                            enim ad minim veniam, quis nostrud exercitation ullamco laboris
                            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                            in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                            nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                            sunt in culpa qui officia deserunt mollit anim id est laborum.
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                            enim ad minim veniam, quis nostrud exercitation ullamco laboris
                            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                            in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                            nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                            sunt in culpa qui officia deserunt mollit anim id est laborum.
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                            enim ad minim veniam, quis nostrud exercitation ullamco laboris
                            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                            in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                            nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                            sunt in culpa qui officia deserunt mollit anim id est laborum."

                            <span>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                                in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                                nulla pariatur."</span>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'indexHidenavscroll',
    mounted() {
        var prevScrollpos = window.pageYOffset;
        window.onscroll = function () {
            var currentScrollPos = window.pageYOffset;
            if (prevScrollpos > currentScrollPos) {
                elems = document.getElementsByClassName('page-header');

                for (i = 0; i < elems.length; i += 1) {
                    elems[i].style.display = '';
                }
            } else {
                var elems = document.getElementsByClassName('page-header');

                for (var i = 0; i < elems.length; i += 1) {
                    elems[i].style.display = 'none';
                }

            }
            prevScrollpos = currentScrollPos;
        }

        var x = document.getElementsByClassName('page-body-wrapper');

        for (var i = 0; i < x.length; i++) {
            x[i].className += ' scorlled';
        }
    },
    unmounted() {
        var elems = document.getElementsByClassName('page-header');
        for (var i = 0; i < elems.length; i += 1) {
            elems[i].style.display = '';
        }
        var x = document.getElementsByClassName('page-body-wrapper scorlled');

        for (i = 0; i < x.length; i++) {
            x[i].className = 'page-body-wrapper';
        }
    }
}
</script>
