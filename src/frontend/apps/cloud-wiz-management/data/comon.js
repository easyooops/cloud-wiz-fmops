import { useLocalStorage } from "@vueuse/core";
import moment from "moment";
import { storeToRefs } from "pinia";
import { useLayoutStore } from "~/store/layout";
//var { primaryColor: primary, secondaryColor: secondary } = storeToRefs(useLayoutStore())
var primary = "#7366ff",
    secondary = "#f73164";
if (process.client) {
}
var series = {
    monthDataSeries1: {
        prices: [8107, 8300, 8260, 8400, 8350, 8500, 8350],
        dates: [
            "13 Nov 2017",
            "14 Nov 2017",
            "15 Nov 2017",
            "16 Nov 2017",
            "17 Nov 2017",
            "20 Nov 2017",
            "21 Nov 2017",
        ],
    },
};
function generateData(baseval, count, yrange) {
    var i = 0;
    var series = [];
    while (i < count) {
        var x = Math.floor(Math.random() * (750 - 1 + 1)) + 1;
        var y =
            Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
            yrange.min;
        var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;

        series.push([x, y, z]);
        baseval += 86400000;
        i++;
    }
    return series;
}
export var cryptoDashboard = computed(() => {
    return {
        options: {
            chart: {
                height: 130,
                type: "radialBar",
                dropShadow: {
                    enabled: true,
                    top: 3,
                    left: 0,
                    blur: 10,
                    color: "var(--theme-deafult)",
                    opacity: 0.35,
                },
            },
            plotOptions: {
                radialBar: {
                    hollow: {
                        size: "60%",
                    },
                    track: {
                        strokeWidth: "60%",
                        opacity: 1,
                        margin: 5,
                    },
                    dataLabels: {
                        showOn: "always",
                        value: {
                            color: "var(--body-font-color)",
                            fontSize: "14px",
                            show: true,
                            offsetY: -10,
                        },
                    },
                },
            },
            colors: ["var(--theme-deafult)"],
            stroke: {
                lineCap: "round",
            },
            responsive: [
                {
                    breakpoint: 2000,
                    options: {
                        chart: {
                            height: "70%",
                        },
                    },
                },
                {
                    breakpoint: 1500,
                    options: {
                        chart: {
                            height: 130,
                        },
                    },
                },
            ],
        },
        series: [78],
        options1: {
            chart: {
                height: 130,
                type: "radialBar",
                dropShadow: {
                    enabled: true,
                    top: 3,
                    left: 0,
                    blur: 10,
                    color: "var(--theme-secondary)",
                    opacity: 0.35,
                },
            },
            plotOptions: {
                radialBar: {
                    hollow: {
                        size: "60%",
                    },
                    track: {
                        strokeWidth: "60%",
                        opacity: 1,
                        margin: 5,
                    },
                    dataLabels: {
                        showOn: "always",
                        value: {
                            color: "var(--body-font-color)",
                            fontSize: "14px",
                            show: true,
                            offsetY: -10,
                        },
                    },
                },
            },
            colors: ["#FFA941"],
            stroke: {
                lineCap: "round",
            },
            responsive: [
                {
                    breakpoint: 2000,
                    options: {
                        chart: {
                            height: "70%",
                        },
                    },
                },
                {
                    breakpoint: 1500,
                    options: {
                        chart: {
                            height: 130,
                        },
                    },
                },
            ],
        },
        series1: [80],
        options2: {
            chart: {
                height: 50,
                type: "radialBar",
                dropShadow: {
                    enabled: true,
                    top: 3,
                    left: 0,
                    blur: 10,
                    color: "#54BA4A",
                    opacity: 0.35,
                },
            },
            plotOptions: {
                radialBar: {
                    hollow: {
                        size: "60%",
                    },
                    track: {
                        strokeWidth: "60%",
                        opacity: 1,
                        margin: 5,
                    },
                    dataLabels: {
                        showOn: "always",
                        value: {
                            color: "var(--body-font-color)",
                            fontSize: "14px",
                            show: true,
                            offsetY: -10,
                        },
                    },
                },
            },
            colors: ["#54BA4A"],
            stroke: {
                lineCap: "round",
            },

            responsive: [
                {
                    breakpoint: 2000,
                    options: {
                        chart: {
                            height: "70%",
                        },
                    },
                },
                {
                    breakpoint: 1500,
                    options: {
                        chart: {
                            height: 130,
                        },
                    },
                },
            ],
        },
        series2: [48],
        options3: {
            chart: {
                width: 120,
                height: 120,
                type: "line",
                toolbar: {
                    show: false,
                },
                offsetY: 10,
                dropShadow: {
                    enabled: true,
                    enabledOnSeries: undefined,
                    top: 6,
                    left: 0,
                    blur: 6,
                    color: "#FFA941",
                    opacity: 0.3,
                },
            },
            grid: {
                show: false,
            },
            colors: ["#FFA941"],
            stroke: {
                width: 2,
                curve: "smooth",
            },
            labels: [
                "jan",
                "feb",
                "mar",
                "apr",
                "may",
                "jun",
                "jul",
                "aug",
                "sep",
                "oct",
                "nov",
            ],
            markers: {
                size: 0,
            },
            xaxis: {
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                },
                tooltip: {
                    enabled: false,
                },
            },
            yaxis: {
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                },
            },
            legend: {
                show: false,
            },
            tooltip: {
                marker: {
                    show: false,
                },
                x: {
                    show: false,
                },
                y: {
                    show: false,
                    labels: {
                        show: false,
                    },
                },
            },
            responsive: [
                {
                    breakpoint: 1790,
                    options: {
                        chart: {
                            width: 100,
                            height: 100,
                        },
                    },
                },
                {
                    breakpoint: 1661,
                    options: {
                        chart: {
                            width: "100%",
                            height: 100,
                        },
                    },
                },
            ],
        },
        series3: [
            {
                data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39],
            },
        ],
        options4: {
            chart: {
                width: 120,
                height: 120,
                type: "line",
                toolbar: {
                    show: false,
                },
                offsetY: 10,
                dropShadow: {
                    enabled: true,
                    enabledOnSeries: undefined,
                    top: 6,
                    left: 0,
                    blur: 6,
                    color: "var(--theme-deafult)",
                    opacity: 0.3,
                },
            },
            grid: {
                show: false,
            },
            colors: ["var(--theme-deafult)"],
            stroke: {
                width: 2,
                curve: "smooth",
            },
            labels: [
                "jan",
                "feb",
                "mar",
                "apr",
                "may",
                "jun",
                "jul",
                "aug",
                "sep",
            ],
            markers: {
                size: 0,
            },
            xaxis: {
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                },
                tooltip: {
                    enabled: false,
                },
            },
            yaxis: {
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                },
            },
            legend: {
                show: false,
            },
            tooltip: {
                marker: {
                    show: false,
                },
                x: {
                    show: false,
                },
                y: {
                    show: false,
                    labels: {
                        show: false,
                    },
                },
            },
            responsive: [
                {
                    breakpoint: 1790,
                    options: {
                        chart: {
                            width: 100,
                            height: 100,
                        },
                    },
                },
                {
                    breakpoint: 1661,
                    options: {
                        chart: {
                            width: "100%",
                            height: 100,
                        },
                    },
                },
            ],
        },
        series4: [
            {
                data: [30, 25, 30, 25, 64, 40, 59, 52, 64],
            },
        ],
        options5: {
            chart: {
                width: 120,
                height: 120,
                type: "line",
                toolbar: {
                    show: false,
                },
                offsetY: 10,
                dropShadow: {
                    enabled: true,
                    enabledOnSeries: undefined,
                    top: 6,
                    left: 0,
                    blur: 6,
                    color: "#54BA4A",
                    opacity: 0.3,
                },
            },
            grid: {
                show: false,
            },
            colors: ["#54BA4A"],
            stroke: {
                width: 2,
                curve: "smooth",
            },
            labels: [
                "jan",
                "feb",
                "mar",
                "apr",
                "may",
                "jun",
                "jul",
                "aug",
                "sep",
                "oct",
            ],
            markers: {
                size: 0,
            },
            xaxis: {
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                },
                tooltip: {
                    enabled: false,
                },
            },
            yaxis: {
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                },
            },
            legend: {
                show: false,
            },
            tooltip: {
                marker: {
                    show: false,
                },
                x: {
                    show: false,
                },
                y: {
                    show: false,
                    labels: {
                        show: false,
                    },
                },
            },
            responsive: [
                {
                    breakpoint: 1790,
                    options: {
                        chart: {
                            width: 100,
                            height: 100,
                        },
                    },
                },
                {
                    breakpoint: 1661,
                    options: {
                        chart: {
                            width: "100%",
                            height: 100,
                        },
                    },
                },
            ],
        },
        series5: [
            {
                data: [30, 25, 36, 30, 64, 50, 45, 62, 60, 64],
            },
        ],
        options6: {
            chart: {
                height: 300,
                type: "line",
                stacked: false,
                toolbar: {
                    show: false,
                },
                dropShadow: {
                    enabled: true,
                    enabledOnSeries: [1],
                    top: 0,
                    left: 0,
                    blur: 15,
                    color: "var(--theme-deafult)",
                    opacity: 0.3,
                },
            },
            stroke: {
                width: [0, 3],
                curve: "smooth",
            },
            dataLabels: {
                enabled: true,
                enabledOnSeries: [1],
            },
            colors: ["rgba(170, 175, 203, 0.2)", "var(--theme-deafult)"],
            grid: {
                borderColor: "var(--chart-border)",
            },
            plotOptions: {
                bar: {
                    columnWidth: "20%",
                },
            },

            fill: {
                type: ["solid", "gradient"],
                gradient: {
                    shade: "light",
                    type: "vertical",
                    shadeIntensity: 0.5,
                    gradientToColors: ["var(--theme-deafult)", "#d867ac"],
                    opacityFrom: 0.8,
                    opacityTo: 0.8,
                    colorStops: [
                        {
                            offset: 0,
                            color: "#d867ac",
                            opacity: 1,
                        },
                        {
                            offset: 30,
                            color: "#d867ac",
                            opacity: 1,
                        },
                        {
                            offset: 50,
                            color: "var(--theme-deafult)",
                            opacity: 1,
                        },
                        {
                            offset: 80,
                            color: "var(--theme-deafult)",
                            opacity: 1,
                        },
                        {
                            offset: 100,
                            color: "var(--theme-deafult)",
                            opacity: 1,
                        },
                    ],
                },
            },
            labels: [
                "Sep 10",
                "Sep 15",
                "Sep 20",
                "Sep 25",
                "Sep 30",
                "Oct 05",
                "Oct 10",
                "Oct 15",
                "Oct 20",
                "Oct 25",
            ],
            markers: {
                size: 0,
            },
            yaxis: {
                min: 0,
                max: 20,
                tickAmount: 5,
                labels: {
                    formatter: function (val) {
                        return val + "k";
                    },
                    style: {
                        fontSize: "12px",
                        fontFamily: "Rubik, sans-serif",
                        colors: "var(--chart-text-color)",
                    },
                },
            },
            xaxis: {
                tooltip: {
                    enabled: false,
                },
                labels: {
                    style: {
                        fontSize: "10px",
                        fontFamily: "Rubik, sans-serif",
                        colors: "var(--chart-text-color)",
                    },
                },
            },
            tooltip: {
                shared: true,
                intersect: false,
            },
            legend: {
                show: false,
            },
        },
        series6: [
            {
                name: "TEAM A",
                type: "column",
                data: [4, 8, 4.5, 8, 13, 8.5, 12, 5, 7, 12],
            },
            {
                name: "TEAM C",
                type: "line",
                data: [2, 3, 2, 6, 8, 12, 9, 7, 9, 7],
            },
        ],
        options7: {
            chart: {
                height: 280,
                type: "radialBar",
            },
            plotOptions: {
                radialBar: {
                    dataLabels: {
                        show: false,
                    },
                    track: {
                        background: "var(--chart-progress-light)",
                        opacity: 0.3,
                    },
                    hollow: {
                        margin: 10,
                        size: "40%",
                        image: "/images/dashboard-4/portfolio-bg.png",
                        imageWidth: 230,
                        imageHeight: 230,
                        imageClipped: false,
                    },
                },
            },
            colors: ["#54BA4A", "#FFA539", "#7366FF"],
            labels: ["USD", "BTC", "ETH"],
            fill: {
                type: "gradient",
                gradient: {
                    shade: "light",
                    type: "horizontal",
                    shadeIntensity: 0.25,
                    inverseColors: true,
                    opacityFrom: 1,
                    opacityTo: 1,
                    stops: [50, 0, 80, 100],
                },
            },
            responsive: [
                {
                    breakpoint: 1500,
                    options: {
                        chart: {
                            height: 260,
                        },
                        plotOptions: {
                            radialBar: {
                                hollow: {
                                    margin: 10,
                                    size: "40%",
                                    image: "/images/dashboard-4/portfolio-bg.png",
                                    imageWidth: 190,
                                    imageHeight: 190,
                                    imageClipped: false,
                                },
                            },
                        },
                    },
                },
                {
                    breakpoint: 1400,
                    options: {
                        chart: {
                            height: 320,
                        },
                        plotOptions: {
                            radialBar: {
                                hollow: {
                                    imageWidth: 260,
                                    imageHeight: 260,
                                },
                            },
                        },
                    },
                },
                {
                    breakpoint: 650,
                    options: {
                        chart: {
                            height: 280,
                        },
                        plotOptions: {
                            radialBar: {
                                hollow: {
                                    imageWidth: 220,
                                    imageHeight: 220,
                                },
                            },
                        },
                    },
                },
            ],
        },
        series7: [44, 55, 67],
    };
});

export var apexDashboard = computed(() => {
    return {
        options: {
            chart: {
                type: "bar",
                width: 180,
                height: 120,
                stacked: true,
                toolbar: {
                    show: false,
                },
            },
            plotOptions: {
                bar: {
                    vertical: true,
                    columnWidth: "40%",
                    barHeight: "80%",
                    startingShape: "rounded",
                    endingShape: "rounded",
                },
            },
            colors: [primary, primary, "#F2F3F7", "#F2F3F7"],
            dataLabels: {
                enabled: false,
            },
            stroke: {
                width: 0,
            },
            legend: {
                show: false,
            },
            grid: {
                xaxis: {
                    offsetX: -2,
                    lines: {
                        show: false,
                    },
                },
                yaxis: {
                    lines: {
                        show: false,
                    },
                },
            },
            yaxis: {
                min: -5,
                max: 5,
                show: false,
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
            },
            tooltip: {
                shared: false,
                x: {
                    show: false,
                },
                y: {
                    show: false,
                },
                z: {
                    show: false,
                },
            },
            xaxis: {
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "July",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
                offsetX: 0,
                offsetY: 0,
                labels: {
                    offsetX: 0,
                    offsetY: 0,
                    show: false,
                },
                axisBorder: {
                    offsetX: 0,
                    offsetY: 0,
                    show: false,
                },
                axisTicks: {
                    offsetX: 0,
                    offsetY: 0,
                    show: false,
                },
            },
            responsive: [
                {
                    breakpoint: 1760,
                    options: {
                        chart: {
                            width: 160,
                        },
                    },
                },
                {
                    breakpoint: 1601,
                    options: {
                        chart: {
                            height: 110,
                        },
                    },
                },
                {
                    breakpoint: 1560,
                    options: {
                        chart: {
                            width: 140,
                        },
                    },
                },
                {
                    breakpoint: 1460,
                    options: {
                        chart: {
                            width: 120,
                        },
                    },
                },
                {
                    breakpoint: 1400,
                    options: {
                        chart: {
                            width: 290,
                        },
                    },
                },
                {
                    breakpoint: 1110,
                    options: {
                        chart: {
                            width: 200,
                        },
                    },
                },
                {
                    breakpoint: 700,
                    options: {
                        chart: {
                            width: 150,
                        },
                    },
                },
                {
                    breakpoint: 576,
                    options: {
                        chart: {
                            width: 220,
                        },
                    },
                },
                {
                    breakpoint: 420,
                    options: {
                        chart: {
                            width: 150,
                        },
                    },
                },
            ],
        },
        series: [
            {
                name: "Daily",
                data: [
                    2.15, 3, 1.5, 2, 2.4, 3, 2.4, 2.8, 1.5, 1.7, 3, 2.5, 3, 2,
                    2.15, 3, 1.1,
                ],
            },
            {
                name: "Weekly",
                data: [
                    -2.15, -3, -1.5, -2, -2.4, -3, -2.4, -2.8, -1.5, -1.7, -3,
                    -2.5, -3, -2, -2.15, -3, -1.1,
                ],
            },
            {
                name: "Monthly",
                data: [
                    -2.25, -2.35, -2.45, -2.55, -2.65, -2.75, -2.85, -2.95,
                    -3.0, -3.1, -3.2, -3.25, -3.1, -3.0, -2.95, -2.85, -2.75,
                ],
            },
            {
                name: "Yearly",
                data: [
                    2.25, 2.35, 2.45, 2.55, 2.65, 2.75, 2.85, 2.95, 3.0, 3.1,
                    3.2, 3.25, 3.1, 3.0, 2.95, 2.85, 2.75,
                ],
            },
        ],
        options2: {
            chart: {
                width: 200,
                height: 150,
                type: "line",
                toolbar: {
                    show: false,
                },
                dropShadow: {
                    enabled: true,
                    enabledOnSeries: undefined,
                    top: 5,
                    left: 0,
                    blur: 3,
                    color: "#16C7F9",
                    opacity: 0.3,
                },
                zoom: {
                    enabled: false,
                },
            },
            colors: ["#16C7F9"],
            dataLabels: {
                enabled: false,
            },
            stroke: {
                width: 2,
                curve: "smooth",
            },
            grid: {
                show: false,
            },
            tooltip: {
                x: {
                    show: false,
                },
                y: {
                    show: false,
                },
                z: {
                    show: false,
                },
                marker: {
                    show: false,
                },
            },
            xaxis: {
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                ],
                labels: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                tooltip: {
                    enabled: false,
                },
            },
            yaxis: {
                labels: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
            },
            responsive: [
                {
                    breakpoint: 1780,
                    options: {
                        chart: {
                            width: 180,
                        },
                    },
                },
                {
                    breakpoint: 1680,
                    options: {
                        chart: {
                            width: 160,
                        },
                    },
                },
                {
                    breakpoint: 1601,
                    options: {
                        chart: {
                            height: 110,
                        },
                    },
                },
                {
                    breakpoint: 1560,
                    options: {
                        chart: {
                            width: 140,
                        },
                    },
                },
                {
                    breakpoint: 1460,
                    options: {
                        chart: {
                            width: 120,
                        },
                    },
                },
                {
                    breakpoint: 1400,
                    options: {
                        chart: {
                            width: 290,
                        },
                    },
                },
                {
                    breakpoint: 1110,
                    options: {
                        chart: {
                            width: 200,
                        },
                    },
                },
                {
                    breakpoint: 700,
                    options: {
                        chart: {
                            width: 150,
                        },
                    },
                },
                {
                    breakpoint: 576,
                    options: {
                        chart: {
                            width: 220,
                        },
                    },
                },
                {
                    breakpoint: 420,
                    options: {
                        chart: {
                            width: 150,
                        },
                    },
                },
            ],
        },
        series2: [
            {
                name: "Desktops",
                data: [210, 180, 650, 200, 600, 100, 800, 300, 500],
            },
        ],
        options3: {
            chart: {
                type: "bar",
                height: 300,
                stacked: true,
                toolbar: {
                    show: false,
                },
                dropShadow: {
                    enabled: true,
                    top: 8,
                    left: 0,
                    blur: 10,
                    color: "#7064F5",
                    opacity: 0.1,
                },
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                    columnWidth: "25px",
                    borderRadius: 0,
                },
            },
            grid: {
                show: true,
                borderColor: "var(--chart-border)",
            },
            dataLabels: {
                enabled: false,
            },
            stroke: {
                width: 2,
                dashArray: 0,
                lineCap: "butt",
                colors: "#fff",
            },
            fill: {
                opacity: 1,
            },
            legend: {
                show: false,
            },
            states: {
                hover: {
                    filter: {
                        type: "darken",
                        value: 1,
                    },
                },
            },
            colors: [primary, "#AAAFCB"],
            yaxis: {
                tickAmount: 3,
                labels: {
                    show: true,
                    style: {
                        fontFamily: "Rubik, sans-serif",
                    },
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
            },
            xaxis: {
                categories: [
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "10",
                    "11",
                    "12",
                    "13",
                    "14",
                    "15",
                    "16",
                    "17",
                    "18",
                    "19",
                    "20",
                    "21",
                ],
                labels: {
                    style: {
                        fontFamily: "Rubik, sans-serif",
                    },
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
            },
            states: {
                hover: {
                    filter: {
                        type: "darken",
                        value: 1,
                    },
                },
            },
            responsive: [
                {
                    breakpoint: 1661,
                    options: {
                        chart: {
                            height: 290,
                        },
                    },
                },
                {
                    breakpoint: 767,
                    options: {
                        plotOptions: {
                            bar: {
                                columnWidth: "35px",
                            },
                        },
                        yaxis: {
                            labels: {
                                show: false,
                            },
                        },
                    },
                },
                {
                    breakpoint: 481,
                    options: {
                        chart: {
                            height: 200,
                        },
                    },
                },
                {
                    breakpoint: 420,
                    options: {
                        chart: {
                            height: 170,
                        },
                        plotOptions: {
                            bar: {
                                columnWidth: "40px",
                            },
                        },
                    },
                },
            ],
        },
        series3: [
            {
                name: "Earning",
                data: [
                    200, 200, 350, 400, 200, 250, 250, 350, 350, 500, 500, 700,
                    850, 700, 400, 400, 250, 250, 400, 350, 400,
                ],
            },
            {
                name: "Expense",
                data: [
                    400, 600, 700, 400, 700, 800, 800, 850, 850, 900, 900, 700,
                    600, 500, 800, 800, 800, 800, 400, 700, 800,
                ],
            },
        ],
        options4: {
            chart: {
                height: 290,
                type: "radialBar",
                toolbar: {
                    show: false,
                },
            },
            plotOptions: {
                radialBar: {
                    hollow: {
                        margin: 0,
                        size: "60%",
                        background: "var(--recent-chart-bg)",
                        image: undefined,
                        imageOffsetX: 0,
                        imageOffsetY: 0,
                        position: "front",
                        dropShadow: {
                            enabled: true,
                            top: 3,
                            left: 0,
                            blur: 4,
                            opacity: 0.05,
                        },
                    },
                    track: {
                        background: "#F4F4F4",
                        strokeWidth: "67%",
                        margin: 0,
                        dropShadow: {
                            enabled: true,
                            top: 0,
                            left: 0,
                            blur: 10,
                            color: "#ddd",
                            opacity: 1,
                        },
                    },

                    dataLabels: {
                        show: true,
                        name: {
                            offsetY: 30,
                            show: true,
                            color: "#888",
                            fontSize: "17px",
                            fontWeight: "500",
                            fontFamily: "Rubik, sans-serif",
                        },
                        value: {
                            formatter: function (val) {
                                return parseInt(val);
                            },
                            offsetY: -8,
                            color: "#111",
                            fontSize: "36px",
                            show: true,
                        },
                    },
                },
            },
            fill: {
                type: "gradient",
                gradient: {
                    shade: "dark",
                    type: "horizontal",
                    shadeIntensity: 0.5,
                    opacityFrom: 1,
                    opacityTo: 1,
                    colorStops: [
                        {
                            offset: 0,
                            color: "#7366FF",
                            opacity: 1,
                        },
                        {
                            offset: 20,
                            color: "#3EA4F1",
                            opacity: 1,
                        },
                        {
                            offset: 100,
                            color: "#FFFFFF",
                            opacity: 1,
                        },
                    ],
                },
            },
            stroke: {
                lineCap: "round",
            },
            labels: ["Total Profit"],
            responsive: [
                {
                    breakpoint: 1840,
                    options: {
                        chart: {
                            height: 260,
                        },
                    },
                },
                {
                    breakpoint: 1700,
                    options: {
                        chart: {
                            height: 250,
                        },
                    },
                },
                {
                    breakpoint: 1660,
                    options: {
                        chart: {
                            height: 230,
                            dataLabels: {
                                name: {
                                    fontSize: "15px",
                                },
                            },
                        },
                    },
                },
                {
                    breakpoint: 1561,
                    options: {
                        chart: {
                            height: 275,
                        },
                    },
                },
                {
                    breakpoint: 1400,
                    options: {
                        chart: {
                            height: 360,
                        },
                    },
                },
                {
                    breakpoint: 1361,
                    options: {
                        chart: {
                            height: 300,
                        },
                    },
                },
                {
                    breakpoint: 1200,
                    options: {
                        chart: {
                            height: 230,
                        },
                    },
                },
                {
                    breakpoint: 1007,
                    options: {
                        chart: {
                            height: 240,
                        },
                    },
                },
                {
                    breakpoint: 600,
                    options: {
                        chart: {
                            height: 230,
                        },
                    },
                },
            ],
        },
        series4: [100],
        options5: {
            chart: {
                type: "bar",
                height: 350,
            },
            plotOptions: {
                bar: {
                    horizontal: false,
                },
            },
            dataLabels: {
                enabled: true,
            },
        },
        series5: [
            {
                data: [
                    {
                        x: "Team A",
                        y: [1, 5],
                    },
                    {
                        x: "Team B",
                        y: [4, 6],
                    },
                    {
                        x: "Team C",
                        y: [5, 8],
                    },
                    {
                        x: "Team D",
                        y: [3, 11],
                    },
                ],
            },
            {
                data: [
                    {
                        x: "Team A",
                        y: [2, 6],
                    },
                    {
                        x: "Team B",
                        y: [1, 3],
                    },
                    {
                        x: "Team C",
                        y: [7, 8],
                    },
                    {
                        x: "Team D",
                        y: [5, 9],
                    },
                ],
            },
        ],
        options6: {
            chart: {
                height: 135,
                type: "line",
                toolbar: {
                    show: false,
                },
                dropShadow: {
                    enabled: true,
                    enabledOnSeries: undefined,
                    top: 5,
                    left: 0,
                    blur: 4,
                    color: "#7366ff",
                    opacity: 0.22,
                },
            },
            grid: {
                yaxis: {
                    lines: {
                        show: false,
                    },
                },
            },
            colors: ["#5527FF"],
            stroke: {
                width: 3,
                curve: "smooth",
            },
            xaxis: {
                type: "category",
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                    "Jan",
                ],
                tickAmount: 10,
                labels: {
                    style: {
                        fontFamily: "Rubik, sans-serif",
                    },
                },
                axisTicks: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
                tooltip: {
                    enabled: false,
                },
            },
            fill: {
                type: "gradient",
                gradient: {
                    shade: "dark",
                    gradientToColors: ["#5527FF"],
                    shadeIntensity: 1,
                    type: "horizontal",
                    opacityFrom: 1,
                    opacityTo: 1,
                    colorStops: [
                        {
                            offset: 0,
                            color: "#5527FF",
                            opacity: 1,
                        },
                        {
                            offset: 100,
                            color: "#E069AE",
                            opacity: 1,
                        },
                    ],
                },
            },
            yaxis: {
                min: -10,
                max: 40,
                labels: {
                    show: false,
                },
            },
            responsive: [
                {
                    breakpoint: 992,
                    options: {
                        chart: {
                            height: 150,
                        },
                    },
                },
                {
                    breakpoint: 768,
                    options: {
                        chart: {
                            height: 180,
                        },
                    },
                },
            ],
        },
        options7: {
            chart: {
                height: 135,
                type: "line",
                toolbar: {
                    show: false,
                },
                dropShadow: {
                    enabled: true,
                    enabledOnSeries: undefined,
                    top: 5,
                    left: 0,
                    blur: 4,
                    color: "#7366ff",
                    opacity: 0.22,
                },
            },
            grid: {
                yaxis: {
                    lines: {
                        show: false,
                    },
                },
            },
            colors: ["#5527FF"],
            stroke: {
                width: 3,
                curve: "smooth",
            },
            xaxis: {
                type: "category",
                categories: [
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "12",
                    "13",
                    "14",
                    "15",
                    "16",
                    "17",
                    "18",
                ],
                tickAmount: 10,
                labels: {
                    style: {
                        fontFamily: "Rubik, sans-serif",
                    },
                },
                axisTicks: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
                tooltip: {
                    enabled: false,
                },
            },
            fill: {
                type: "gradient",
                gradient: {
                    shade: "dark",
                    gradientToColors: ["#5527FF"],
                    shadeIntensity: 1,
                    type: "horizontal",
                    opacityFrom: 1,
                    opacityTo: 1,
                    colorStops: [
                        {
                            offset: 0,
                            color: "#5527FF",
                            opacity: 1,
                        },
                        {
                            offset: 100,
                            color: "#E069AE",
                            opacity: 1,
                        },
                    ],
                },
            },
            yaxis: {
                min: -10,
                max: 40,
                labels: {
                    show: false,
                },
            },
            responsive: [
                {
                    breakpoint: 992,
                    options: {
                        chart: {
                            height: 150,
                        },
                    },
                },
                {
                    breakpoint: 768,
                    options: {
                        chart: {
                            height: 180,
                        },
                    },
                },
            ],
        },
        series6: [
            {
                name: "Growth",
                data: [10, 5, 15, 0, 15, 12, 29, 29, 29, 12, 15, 5],
            },
        ],
    };
});
export const ecomDashboard = {
    options: {
        chart: {
            height: 235,
            type: "line",
            toolbar: {
                show: false,
            },
        },
        colors: [
            "#7064F5",
            "#7064F5",
            "#7064F5",
            "#7064F5",
            "#7064F5",
            "#7064F5",
            "#7064F5",
            "#7064F5",
            "#7064F5",
            "#7064F5",
            "#7064F5",
            "#7064F5",
        ],
        fill: {
            type: "gradient",
            gradient: {
                shade: "dark",
                type: "horizontal",
                shadeIntensity: 1,
                gradientToColors: [
                    "#FF8BA7",
                    "#FF8BA7",
                    "#FF8BA7",
                    "#FF8BA7",
                    "#FF8BA7",
                    "#FF8BA7",
                    "#FF8BA7",
                    "#FF8BA7",
                    "#FF8BA7",
                    "#FF8BA7",
                    "#FF8BA7",
                    "#FF8BA7",
                ],
                inverseColors: true,
                opacityFrom: 1,
                opacityTo: 1,
                colorStops: [
                    {
                        offset: 0,
                        color: "#e183b7",
                        opacity: 1,
                    },
                    {
                        offset: 20,
                        color: "#ff8ba7",
                        opacity: 1,
                    },
                    {
                        offset: 30,
                        color: "#b377d0",
                        opacity: 1,
                    },
                    {
                        offset: 65,
                        color: "#7064f5",
                        opacity: 1,
                    },
                    {
                        offset: 70,
                        color: "#b778cf",
                        opacity: 1,
                    },
                    {
                        offset: 80,
                        color: "#eb86b2",
                        opacity: 1,
                    },
                    {
                        offset: 100,
                        color: "#a873d7",
                        opacity: 1,
                    },
                ],
            },
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            curve: "smooth",
            width: 2,
        },
        grid: {
            borderColor: "#e7e7e7",
            yaxis: {
                lines: {
                    show: false,
                },
            },
            column: {
                colors: ["transparent", "var(--light-background)"],
                opacity: 0.5,
            },
        },
        xaxis: {
            categories: [
                "01",
                "03",
                "05",
                "07",
                "09",
                "10",
                "11",
                "12",
                "15",
                "16",
                "18",
            ],
            tickAmount: 6,
            tickPlacement: "between",
            axisTicks: {
                show: false,
            },
            axisBorder: {
                show: false,
            },
            tooltip: {
                enabled: false,
            },
        },
        yaxis: {
            min: 5,
            max: 40,
            axisBorder: {
                show: true,
                color: "var(--chart-border)",
                offsetX: 12,
                offsetY: 5,
            },
        },
        legend: {
            show: false,
        },
        tooltip: {
            shared: false,
        },
        responsive: [
            {
                breakpoint: 1400,
                options: {
                    chart: {
                        height: 230,
                    },
                },
            },
        ],
    },
    series: [
        {
            name: "Sales",
            data: [23, 23, 20, 20, 32, 32, 40, 32, 32, 25, 30, 30],
        },
        {
            name: "sales",
            data: [22, 22, 19, 19, 31, 31, 39, 31, 31, 24, 29, 29],
        },
        {
            name: "sales",
            data: [21, 21, 18, 18, 30, 30, 38, 30, 30, 23, 28, 28],
        },
        {
            name: "sales",
            data: [20, 20, 17, 17, 29, 29, 37, 29, 29, 22, 27, 27],
        },
        {
            name: "sales",
            data: [19, 19, 16, 16, 28, 28, 36, 28, 28, 21, 26, 26],
        },
        {
            name: "sales",
            data: [18, 18, 15, 15, 27, 27, 35, 27, 27, 20, 25, 25],
        },
        {
            name: "sales",
            data: [17, 17, 14, 14, 26, 26, 34, 26, 26, 19, 24, 24],
        },
        {
            name: "sales",
            data: [16, 16, 13, 13, 25, 25, 33, 25, 25, 18, 23, 23],
        },
        {
            name: "sales",
            data: [16, 16, 13, 13, 25, 25, 33, 25, 25, 18, 23, 23],
        },
        {
            name: "sales",
            data: [15, 15, 12, 12, 24, 24, 32, 24, 24, 17, 22, 22],
        },
        {
            name: "sales",
            data: [14, 14, 11, 11, 23, 23, 31, 23, 23, 16, 21, 21],
        },
        {
            name: "sales",
            data: [13, 13, 10, 10, 22, 22, 30, 22, 22, 15, 20, 20],
        },
    ],
    options1: {
        labels: ["Shoes", "Grocery", "other"],

        chart: {
            type: "donut",
            height: 300,
        },
        dataLabels: {
            enabled: false,
        },
        legend: {
            position: "bottom",
            fontSize: "14px",
            fontFamily: "Rubik, sans-serif",
            fontWeight: 500,
            labels: {
                colors: ["var(--chart-text-color)"],
            },
            markers: {
                width: 6,
                height: 6,
            },
            itemMargin: {
                horizontal: 7,
                vertical: 0,
            },
        },
        stroke: {
            width: 10,
            colors: ["var(--light2)"],
        },
        plotOptions: {
            pie: {
                expandOnClick: false,
                donut: {
                    size: "83%",
                    labels: {
                        show: true,
                        name: {
                            offsetY: 4,
                        },
                        total: {
                            show: true,
                            fontSize: "20px",
                            fontFamily: "Rubik, sans-serif",
                            fontWeight: 500,
                            label: "$ 34,098",
                            formatter: () => "Total Profit",
                        },
                    },
                },
            },
        },
        states: {
            normal: {
                filter: {
                    type: "none",
                },
            },
            hover: {
                filter: {
                    type: "none",
                },
            },
            active: {
                allowMultipleDataPointsSelection: false,
                filter: {
                    type: "none",
                },
            },
        },
        colors: ["#54BA4A", "var(--theme-deafult)", "#FFA941"],
        responsive: [
            {
                breakpoint: 1630,
                options: {
                    chart: {
                        height: 360,
                    },
                },
            },
            {
                breakpoint: 1584,
                options: {
                    chart: {
                        height: 400,
                    },
                },
            },
            {
                breakpoint: 1473,
                options: {
                    chart: {
                        height: 250,
                    },
                },
            },
            {
                breakpoint: 1425,
                options: {
                    chart: {
                        height: 270,
                    },
                },
            },
            {
                breakpoint: 1400,
                options: {
                    chart: {
                        height: 320,
                    },
                },
            },
            {
                breakpoint: 480,
                options: {
                    chart: {
                        height: 250,
                    },
                },
            },
        ],
    },
    series1: [30, 55, 35],
    options2: {
        chart: {
            height: 300,
            type: "line",
            stacked: false,
            toolbar: {
                show: false,
            },
            dropShadow: {
                enabled: true,
                top: 2,
                left: 0,
                blur: 4,
                color: "#000",
                opacity: 0.08,
            },
        },
        stroke: {
            width: [2, 2, 2],
            curve: "smooth",
        },
        grid: {
            show: true,
            borderColor: "var(--chart-border)",
            strokeDashArray: 0,
            position: "back",
            xaxis: {
                lines: {
                    show: true,
                },
            },
            padding: {
                top: 0,
                right: 0,
                bottom: 0,
                left: 0,
            },
        },
        plotOptions: {
            bar: {
                columnWidth: "50%",
            },
        },
        colors: ["#7064F5", "#54BA4A", "#FF3364"],
        fill: {
            type: "gradient",
            gradient: {
                shade: "light",
                type: "vertical",
                opacityFrom: 0.4,
                opacityTo: 0,
                stops: [0, 100],
            },
        },
        labels: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
        ],
        markers: {
            discrete: [
                {
                    seriesIndex: 0,
                    dataPointIndex: 2,
                    fillColor: "#7064F5",
                    strokeColor: "var(--white)",
                    size: 5,
                    sizeOffset: 3,
                },
                {
                    seriesIndex: 1,
                    dataPointIndex: 2,
                    fillColor: "#54BA4A",
                    strokeColor: "var(--white)",
                    size: 5,
                },
                {
                    seriesIndex: 2,
                    dataPointIndex: 2,
                    fillColor: "#FF3364",
                    strokeColor: "var(--white)",
                    size: 5,
                },
                {
                    seriesIndex: 0,
                    dataPointIndex: 5,
                    fillColor: "#7064F5",
                    strokeColor: "var(--white)",
                    size: 5,
                    sizeOffset: 3,
                },
                {
                    seriesIndex: 1,
                    dataPointIndex: 5,
                    fillColor: "#54BA4A",
                    strokeColor: "var(--white)",
                    size: 5,
                },
                {
                    seriesIndex: 2,
                    dataPointIndex: 5,
                    fillColor: "#FF3364",
                    strokeColor: "var(--white)",
                    size: 5,
                },
                {
                    seriesIndex: 0,
                    dataPointIndex: 9,
                    fillColor: "#7064F5",
                    strokeColor: "var(--white)",
                    size: 5,
                    sizeOffset: 3,
                },
                {
                    seriesIndex: 1,
                    dataPointIndex: 9,
                    fillColor: "#54BA4A",
                    strokeColor: "var(--white)",
                    size: 5,
                },
                {
                    seriesIndex: 2,
                    dataPointIndex: 9,
                    fillColor: "#FF3364",
                    strokeColor: "var(--white)",
                    size: 5,
                },
            ],
            hover: {
                size: 5,
                sizeOffset: 0,
            },
        },
        xaxis: {
            type: "category",
            tickAmount: 4,
            tickPlacement: "between",
            tooltip: {
                enabled: false,
            },
            axisBorder: {
                color: "var(--chart-border)",
            },
            axisTicks: {
                show: false,
            },
        },
        legend: {
            show: false,
        },
        yaxis: {
            min: 0,
            tickAmount: 6,
            tickPlacement: "between",
        },
        tooltip: {
            shared: false,
            intersect: false,
        },
        responsive: [
            {
                breakpoint: 1200,
                options: {
                    chart: {
                        height: 250,
                    },
                },
            },
        ],
    },
    series2: [
        {
            name: "Earning",
            type: "area",
            data: [44, 55, 35, 50, 67, 50, 55, 45, 32, 38, 45],
        },
        {
            name: "Order",
            type: "area",
            data: [35, 30, 23, 40, 50, 35, 40, 52, 67, 50, 55],
        },
        {
            name: "Refunds",
            type: "area",
            data: [25, 20, 15, 25, 32, 20, 30, 35, 23, 30, 20],
        },
    ],
    options3: {
        chart: {
            type: "bar",
            height: 180,
            toolbar: {
                show: false,
            },
        },
        plotOptions: {
            bar: {
                horizontal: false,
                columnWidth: "55%",
            },
        },
        colors: ["var(--light-bg)"],
        grid: {
            show: false,
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            show: true,
            width: 2,
            colors: ["transparent"],
        },
        xaxis: {
            categories: [
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
            ],
            labels: {
                show: false,
            },
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
        },
        yaxis: {
            labels: {
                show: false,
            },
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
        },
        fill: {
            opacity: 0.7,
        },
        tooltip: {
            enabled: false,
        },
        states: {
            normal: {
                filter: {
                    type: "none",
                },
            },
            hover: {
                filter: {
                    type: "none",
                },
            },
            active: {
                allowMultipleDataPointsSelection: false,
                filter: {
                    type: "none",
                },
            },
        },
        responsive: [
            {
                breakpoint: 405,
                options: {
                    chart: {
                        height: 150,
                    },
                },
            },
        ],
    },
    series3: [
        {
            name: "Revenue",
            data: [
                30, 40, 18, 25, 18, 10, 20, 35, 22, 40, 30, 38, 20, 35, 11, 28,
                40, 11, 28, 40, 11, 28, 40, 11, 28, 40, 11,
            ],
        },
    ],
    options4: {
        chart: {
            type: "bar",
            height: 270,
            toolbar: {
                show: false,
            },
        },
        plotOptions: {
            bar: {
                horizontal: false,
                columnWidth: "50%",
            },
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            show: true,
            width: 6,
            colors: ["transparent"],
        },
        grid: {
            show: true,
            borderColor: "var(--chart-border)",
            xaxis: {
                lines: {
                    show: true,
                },
            },
        },
        colors: ["#FFA941", "var(--theme-deafult)"],
        xaxis: {
            categories: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            tickAmount: 4,
            tickPlacement: "between",
            labels: {
                style: {
                    fontFamily: "Rubik, sans-serif",
                },
            },
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
        },
        yaxis: {
            min: 0,
            max: 100,
            tickAmount: 5,
            tickPlacement: "between",
            labels: {
                style: {
                    fontFamily: "Rubik, sans-serif",
                },
            },
        },
        fill: {
            opacity: 1,
        },
        legend: {
            position: "top",
            horizontalAlign: "left",
            fontFamily: "Rubik, sans-serif",
            fontSize: "14px",
            fontWeight: 500,
            labels: {
                colors: "var(--chart-text-color)",
            },
            markers: {
                width: 6,
                height: 6,
                radius: 12,
            },
            itemMargin: {
                horizontal: 10,
            },
        },
        responsive: [
            {
                breakpoint: 1366,
                options: {
                    plotOptions: {
                        bar: {
                            columnWidth: "80%",
                        },
                    },
                    grid: {
                        padding: {
                            right: 0,
                        },
                    },
                },
            },
            {
                breakpoint: 992,
                options: {
                    plotOptions: {
                        bar: {
                            columnWidth: "70%",
                        },
                    },
                },
            },
            {
                breakpoint: 576,
                options: {
                    plotOptions: {
                        bar: {
                            columnWidth: "60%",
                        },
                    },
                    grid: {
                        padding: {
                            right: 5,
                        },
                    },
                },
            },
        ],
    },
    series4: [
        {
            name: "Active",
            data: [18, 10, 65, 18, 28, 10],
        },
        {
            name: "Bounce",
            data: [25, 50, 30, 30, 25, 45],
        },
    ],
};
export const onlineDashboard = {
    options: {
        chart: {
            width: 240,
            height: 360,
            type: "radialBar",
            offsetX: -28,
        },
        plotOptions: {
            radialBar: {
                dataLabels: {
                    name: {
                        offsetY: 20,
                        color: "var(--chart-text-color)",
                        fontFamily: "Rubik, sans-serif",
                        fontWeight: 500,
                    },
                    value: {
                        fontSize: "22px",
                        offsetY: -16,
                        fontFamily: "Rubik, sans-serif",
                        fontWeight: 500,
                    },
                    total: {
                        show: true,
                        label: "Task Done!",
                        fontSize: "12px",
                        formatter: function () {
                            return "89%";
                        },
                    },
                },
                hollow: {
                    margin: 5,
                    size: "70%",
                    image: "/images/dashboard-3/round.png",
                    imageWidth: 115,
                    imageHeight: 115,
                    imageClipped: false,
                },
                track: {
                    background: "transparent",
                },
            },
        },
        colors: ["var(--theme-deafult)", "#FFA941"],
        labels: ["Progress", "Done"],
        stroke: {
            lineCap: "round",
        },
        legend: {
            show: true,
            position: "bottom",
            horizontalAlign: "center",
            offsetY: -15,
            fontSize: "14px",
            fontFamily: "Rubik, sans-serif",
            fontWeight: 500,
            labels: {
                colors: "var(--chart-text-color)",
            },
            markers: {
                width: 6,
                height: 6,
            },
        },
        responsive: [
            {
                breakpoint: 1830,
                options: {
                    chart: {
                        offsetX: -40,
                    },
                },
            },
            {
                breakpoint: 1750,
                options: {
                    chart: {
                        offsetX: -50,
                    },
                },
            },
            {
                breakpoint: 1661,
                options: {
                    chart: {
                        offsetX: -10,
                    },
                },
            },
            {
                breakpoint: 1530,
                options: {
                    chart: {
                        offsetX: -25,
                    },
                },
            },
            {
                breakpoint: 1400,
                options: {
                    chart: {
                        offsetX: 10,
                    },
                },
            },
            {
                breakpoint: 1300,
                options: {
                    chart: {
                        offsetX: -10,
                    },
                },
            },
            {
                breakpoint: 1200,
                options: {
                    chart: {
                        width: 255,
                    },
                },
            },
            {
                breakpoint: 992,
                options: {
                    chart: {
                        width: 245,
                    },
                },
            },
            {
                breakpoint: 600,
                options: {
                    chart: {
                        width: 225,
                    },
                },
            },
        ],
    },
    series: [38, 60],
    options1: {
        chart: {
            height: 315,
            type: "line",
            toolbar: {
                show: false,
            },
        },
        grid: {
            show: true,
            borderColor: "var(--chart-border)",
            xaxis: {
                lines: {
                    show: true,
                },
            },
        },
        colors: [
            "var(--theme-deafult)",
            "#F47DEA",
            "#FFA941",
            "#FFC200",
            "#54BA4A",
            "#3DA831",
            "#57B9F6",
            "#FF3377",
            "#773ACE",
            "#945CFF",
            "#7366ff",
        ],
        stroke: {
            width: 1.5,
            curve: "smooth",
        },
        markers: {
            discrete: [
                {
                    seriesIndex: 0,
                    dataPointIndex: 0,
                    fillColor: "#7064F5",
                    strokeColor: "var(--white)",
                    size: 6,
                },
                {
                    seriesIndex: 1,
                    dataPointIndex: 5,
                    fillColor: "#7064F5",
                    strokeColor: "var(--white)",
                    size: 6,
                },
                {
                    seriesIndex: 2,
                    dataPointIndex: 3,
                    fillColor: "#7064F5",
                    strokeColor: "var(--white)",
                    size: 6,
                },
            ],
        },
        tooltip: {
            shared: false,
            intersect: false,
        },
        xaxis: {
            type: "category",
            categories: [
                "Sep 5",
                "Sep 8",
                "Sep 12",
                "Sep 16",
                "Sep 18",
                "Sep 17",
                "Sep 23",
                "Sep 26",
            ],
            tickAmount: 12,
            labels: {
                style: {
                    colors: "var(--chart-text-color)",
                    fontSize: "12px",
                    fontFamily: "Rubik, sans-serif",
                    fontWeight: 400,
                },
            },
            axisTicks: {
                show: false,
            },
            axisBorder: {
                show: false,
            },
            tooltip: {
                enabled: false,
            },
        },
        fill: {
            type: [
                "solid",
                "solid",
                "solid",
                "solid",
                "solid",
                "solid",
                "solid",
                "solid",
                "solid",
                "solid",
                "gradient",
            ],
            gradient: {
                shade: "light",
                type: "vertical",
                shadeIntensity: 0.5,
                opacityFrom: 0.5,
                opacityTo: 0,
                stops: [0, 80, 100],
            },
        },
        yaxis: {
            min: 0,
            max: 50,
            tickAmount: 5,
            labels: {
                style: {
                    colors: "var(--chart-text-color)",
                    fontSize: "12px",
                    fontFamily: "Rubik, sans-serif",
                    fontWeight: 400,
                },
            },
        },
        legend: {
            show: false,
        },
        responsive: [
            {
                breakpoint: 1661,
                options: {
                    chart: {
                        height: 265,
                    },
                },
            },
        ],
    },
    series1: [
        {
            name: "growth",
            type: "line",
            data: [25, 30, 43, 25, 38, 25, 33, 25],
        },
        {
            name: "growth",
            type: "line",
            data: [25, 30, 41, 25, 36, 25, 31, 25],
        },
        {
            name: "growth",
            type: "line",
            data: [25, 29, 37, 25, 34, 25, 29, 25],
        },
        {
            name: "growth",
            type: "line",
            data: [25, 28, 34, 25, 32, 25, 28, 25],
        },
        {
            name: "growth",
            type: "line",
            data: [25, 27, 30, 25, 28, 25, 27, 25],
        },
        {
            name: "growth",
            type: "line",
            data: [25, 26, 24, 25, 24, 25, 24, 25],
        },
        {
            name: "growth",
            type: "line",
            data: [25, 26, 20, 25, 21, 25, 23, 25],
        },
        {
            name: "growth",
            type: "line",
            data: [25, 24, 16, 25, 18, 25, 22, 25],
        },
        {
            name: "growth",
            type: "line",
            data: [25, 23, 12, 25, 15, 25, 21, 25],
        },
        {
            name: "growth",
            type: "line",
            data: [25, 23, 10, 25, 13, 25, 19, 25],
        },
        {
            name: "growth",
            type: "area",
            data: [25, 28, 37, 25, 33, 25, 27, 25],
        },
    ],
    options2: {
        chart: {
            height: 300,
            type: "bar",
            toolbar: {
                show: false,
            },
            dropShadow: {
                enabled: true,

                top: 10,
                left: 0,
                blur: 5,
                color: "#7064F5",
                opacity: 0.35,
            },
        },
        plotOptions: {
            bar: {
                borderRadius: 6,
                columnWidth: "30%",
            },
        },
        dataLabels: {
            enabled: false,
        },
        xaxis: {
            categories: ["S", "M", "T", "W", "T", "F", "S"],
            labels: {
                style: {
                    fontSize: "12px",
                    fontFamily: "Rubik, sans-serif",
                    colors: "var(--chart-text-color)",
                },
            },
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
            tooltip: {
                enabled: false,
            },
        },
        yaxis: {
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
            labels: {
                formatter: function (val) {
                    return val + " " + "Hr";
                },
                style: {
                    fontSize: "12px",
                    fontFamily: "Rubik, sans-serif",
                    colors: "var(--chart-text-color)",
                },
            },
        },
        grid: {
            borderColor: "var(--chart-dashed-border)",
            strokeDashArray: 5,
        },
        colors: ["#7064F5", "#8D83FF"],
        fill: {
            type: "gradient",
            gradient: {
                shade: "light",
                type: "vertical",
                gradientToColors: ["#7064F5", "#8D83FF"],
                opacityFrom: 0.98,
                opacityTo: 0.85,
                stops: [0, 100],
            },
        },
        responsive: [
            {
                breakpoint: 1200,
                options: {
                    chart: {
                        height: 200,
                    },
                },
            },
        ],
    },
    series2: [
        {
            name: "Activity",
            data: [2, 4, 2.5, 1.5, 5.5, 1.5, 4],
        },
    ],
    options3: {
        chart: {
            type: "bar",
            height: 305,
        },
        plotOptions: {
            bar: {
                horizontal: false,
            },
        },
        dataLabels: {
            enabled: true,
        },
    },
    series3: [
        {
            data: [
                {
                    x: "Team A",
                    y: [1, 5],
                },
                {
                    x: "Team B",
                    y: [4, 6],
                },
                {
                    x: "Team C",
                    y: [5, 8],
                },
                {
                    x: "Team D",
                    y: [3, 11],
                },
            ],
        },
        {
            data: [
                {
                    x: "Team A",
                    y: [2, 6],
                },
                {
                    x: "Team B",
                    y: [1, 3],
                },
                {
                    x: "Team C",
                    y: [7, 8],
                },
                {
                    x: "Team D",
                    y: [5, 9],
                },
            ],
        },
    ],
    options4: {
        chart: {
            type: "donut",
            height: 80,
        },
        colors: [
            "var(--theme-deafult)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
        ],
        legend: {
            show: false,
        },
        stroke: {
            width: 1,
            colors: "var(--white)",
        },
        dataLabels: {
            enabled: false,
        },
        tooltip: {
            enabled: false,
        },
        plotOptions: {
            pie: {
                donut: {
                    labels: {
                        show: true,
                        value: {
                            fontSize: "11px",
                            fontFamily: "Rubik, sans-serif",
                            fontWeight: 400,
                            color: "var(--chart-text-color)",
                            offsetY: -12,
                            formatter: function (val) {
                                return val;
                            },
                        },
                        total: {
                            show: true,
                            showAlways: false,
                            label: "Total",
                            fontSize: "11px",
                            fontFamily: "Rubik, sans-serif",
                        },
                    },
                },
            },
        },
        states: {
            normal: {
                filter: {
                    type: "none",
                },
            },
            hover: {
                filter: {
                    type: "none",
                },
            },
            active: {
                allowMultipleDataPointsSelection: false,
                filter: {
                    type: "none",
                },
            },
        },
    },
    series4: [20, 5, 5, 5, 5, 5, 5],
    options5: {
        chart: {
            type: "donut",
            height: 80,
        },
        colors: [
            "var(--theme-deafult)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
        ],
        legend: {
            show: false,
        },
        stroke: {
            width: 1,
            colors: "var(--white)",
        },
        dataLabels: {
            enabled: false,
        },
        tooltip: {
            enabled: false,
        },
        plotOptions: {
            pie: {
                donut: {
                    labels: {
                        show: true,
                        value: {
                            fontSize: "11px",
                            fontFamily: "Rubik, sans-serif",
                            fontWeight: 400,
                            color: "var(--chart-text-color)",
                            offsetY: -12,
                            formatter: function (val) {
                                return val;
                            },
                        },
                        total: {
                            show: true,
                            showAlways: false,
                            label: "Total",
                            fontSize: "11px",
                            fontFamily: "Rubik, sans-serif",
                        },
                    },
                },
            },
        },
        states: {
            normal: {
                filter: {
                    type: "none",
                },
            },
            hover: {
                filter: {
                    type: "none",
                },
            },
            active: {
                allowMultipleDataPointsSelection: false,
                filter: {
                    type: "none",
                },
            },
        },
    },
    series5: [50, 10, 10, 10],
    options6: {
        chart: {
            type: "donut",
            height: 80,
        },
        colors: [
            "var(--theme-deafult)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
            "var(--chart-progress-light)",
        ],
        legend: {
            show: false,
        },
        stroke: {
            width: 1,
            colors: "var(--white)",
        },
        dataLabels: {
            enabled: false,
        },
        tooltip: {
            enabled: false,
        },
        plotOptions: {
            pie: {
                donut: {
                    labels: {
                        show: true,
                        value: {
                            fontSize: "11px",
                            fontFamily: "Rubik, sans-serif",
                            fontWeight: 400,
                            color: "var(--chart-text-color)",
                            offsetY: -12,
                            formatter: function (val) {
                                return val;
                            },
                        },
                        total: {
                            show: true,
                            showAlways: false,
                            label: "Total",
                            fontSize: "11px",
                            fontFamily: "Rubik, sans-serif",
                        },
                    },
                },
            },
        },
        states: {
            normal: {
                filter: {
                    type: "none",
                },
            },
            hover: {
                filter: {
                    type: "none",
                },
            },
            active: {
                allowMultipleDataPointsSelection: false,
                filter: {
                    type: "none",
                },
            },
        },
    },
    series6: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
};
export const socialDashboard = {
    options: {
        chart: {
            height: 130,
            type: "radialBar",
            dropShadow: {
                enabled: true,
                top: 3,
                left: 0,
                blur: 10,
                color: "var(--theme-deafult)",
                opacity: 0.35,
            },
        },
        plotOptions: {
            radialBar: {
                hollow: {
                    size: "60%",
                },
                track: {
                    strokeWidth: "60%",
                    opacity: 1,
                    margin: 5,
                },
                dataLabels: {
                    showOn: "always",
                    value: {
                        color: "var(--body-font-color)",
                        fontSize: "14px",
                        show: true,
                        offsetY: -10,
                    },
                },
            },
        },
        colors: ["var(--theme-deafult)"],
        stroke: {
            lineCap: "round",
        },
        responsive: [
            {
                breakpoint: 1500,
                options: {
                    chart: {
                        height: 130,
                    },
                },
            },
        ],
    },
    series: [78],
    options1: {
        chart: {
            height: 130,
            type: "radialBar",
            dropShadow: {
                enabled: true,
                top: 3,
                left: 0,
                blur: 10,
                color: "#FFA941",
                opacity: 0.35,
            },
        },
        plotOptions: {
            radialBar: {
                hollow: {
                    size: "60%",
                },
                track: {
                    strokeWidth: "60%",
                    opacity: 1,
                    margin: 5,
                },
                dataLabels: {
                    showOn: "always",
                    value: {
                        color: "var(--body-font-color)",
                        fontSize: "14px",
                        show: true,
                        offsetY: -10,
                    },
                },
            },
        },
        colors: ["#FFA941"],
        stroke: {
            lineCap: "round",
        },
        responsive: [
            {
                breakpoint: 1500,
                options: {
                    chart: {
                        height: 130,
                    },
                },
            },
        ],
    },
    series1: [70],
    options2: {
        chart: {
            height: 130,
            type: "radialBar",
            dropShadow: {
                enabled: true,
                top: 3,
                left: 0,
                blur: 10,
                color: "#57B9F6",
                opacity: 0.35,
            },
        },
        plotOptions: {
            radialBar: {
                hollow: {
                    size: "60%",
                },
                track: {
                    strokeWidth: "60%",
                    opacity: 1,
                    margin: 5,
                },
                dataLabels: {
                    showOn: "always",
                    value: {
                        color: "var(--body-font-color)",
                        fontSize: "14px",
                        show: true,
                        offsetY: -10,
                    },
                },
            },
        },
        colors: ["#57B9F6"],
        stroke: {
            lineCap: "round",
        },
        responsive: [
            {
                breakpoint: 1500,
                options: {
                    chart: {
                        height: 130,
                    },
                },
            },
        ],
    },
    series2: [50],
    options3: {
        chart: {
            height: 265,
            type: "line",
            toolbar: {
                show: false,
            },
            dropShadow: {
                enabled: true,
                top: 8,
                left: 0,
                blur: 2,
                color: ["#FFA941", "#7366FF"],
                opacity: 0.1,
            },
        },
        grid: {
            show: true,
            borderColor: "var(--chart-border)",
            xaxis: {
                lines: {
                    show: true,
                },
            },
        },
        colors: ["#FFA941", "#7366FF"],
        stroke: {
            width: 2,
            curve: "smooth",
            opacity: 1,
        },
        markers: {
            discrete: [
                {
                    seriesIndex: 1,
                    dataPointIndex: 4,
                    fillColor: "#7064F5",
                    strokeColor: "var(--white)",
                    size: 6,
                },
            ],
        },
        tooltip: {
            shared: false,
            intersect: false,
            marker: {
                width: 5,
                height: 5,
            },
        },
        xaxis: {
            type: "category",
            categories: [
                "Sep 5",
                "Sep 8",
                "Sep 12",
                "Sep 16",
                "Sep 18",
                "Sep 17",
                "Sep 23",
                "Sep 26",
                "Sep 30",
            ],
            tickAmount: 12,
            crosshairs: {
                show: false,
            },
            labels: {
                style: {
                    colors: "var(--chart-text-color)",
                    fontSize: "12px",
                    fontFamily: "Rubik, sans-serif",
                    fontWeight: 400,
                },
            },
            axisTicks: {
                show: false,
            },
            axisBorder: {
                show: false,
            },
            tooltip: {
                enabled: false,
            },
        },
        fill: {
            opacity: 1,
            type: "gradient",
            gradient: {
                shade: "light",
                type: "horizontal",
                shadeIntensity: 1,
                opacityFrom: 0.95,
                opacityTo: 1,
                stops: [0, 90, 100],
            },
        },
        yaxis: {
            min: 10,
            max: 60,
            tickAmount: 5,
            labels: {
                style: {
                    colors: "var(--chart-text-color)",
                    fontSize: "12px",
                    fontFamily: "Rubik, sans-serif",
                    fontWeight: 400,
                },
            },
        },
        legend: {
            show: false,
        },
        responsive: [
            {
                breakpoint: 1694,
                options: {
                    chart: {
                        height: 240,
                    },
                },
            },
            {
                breakpoint: 1661,
                options: {
                    chart: {
                        height: 265,
                    },
                },
            },
            {
                breakpoint: 1412,
                options: {
                    chart: {
                        height: 240,
                    },
                },
            },
            {
                breakpoint: 1200,
                options: {
                    chart: {
                        height: 260,
                    },
                },
            },
            {
                breakpoint: 1040,
                options: {
                    chart: {
                        height: 240,
                    },
                },
            },
            {
                breakpoint: 992,
                options: {
                    chart: {
                        height: 255,
                    },
                },
            },
        ],
    },
    series3: [
        {
            name: "growth",
            type: "line",
            data: [12, 10, 25, 12, 30, 10, 55, 45, 60],
        },
        {
            name: "growth",
            type: "line",
            data: [10, 15, 20, 18, 38, 25, 55, 35, 60],
        },
    ],
    options4: {
        chart: {
            width: 125,
            height: 150,
            type: "line",
            zoom: {
                enabled: false,
            },
            toolbar: {
                show: false,
            },
            dropShadow: {
                enabled: true,
                top: 8,
                left: 0,
                blur: 3,
                color: "#54BA4A",
                opacity: 0.2,
            },
        },
        markers: {
            hover: {
                size: 3,
            },
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            curve: "smooth",
            width: 2,
        },
        grid: {
            show: false,
        },
        tooltip: {
            x: {
                show: false,
            },
            z: {
                show: false,
            },
        },
        annotations: {
            points: [
                {
                    x: 90,
                    y: 58,
                    marker: {
                        size: 4,
                        fillColor: "#54BA4A",
                        strokeColor: "var(--white)",
                        radius: 2,
                    },
                },
            ],
        },
        colors: ["#54BA4A"],
        fill: {
            opacity: 1,
            type: "gradient",
            gradient: {
                shade: "light",
                type: "vertical",
                shadeIntensity: 1,
                opacityFrom: 0.95,
                opacityTo: 1,

                colorStops: [
                    {
                        offset: 0,
                        color: "#54BA4A",
                        opacity: 0.1,
                    },
                    {
                        offset: 30,
                        color: "#54BA4A",
                        opacity: 0.8,
                    },
                    {
                        offset: 80,
                        color: "#54BA4A",
                        opacity: 1,
                    },
                    {
                        offset: 100,
                        color: "#54BA4A",
                        opacity: 0.1,
                    },
                ],
            },
        },
        xaxis: {
            categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            labels: {
                show: false,
            },
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
            tooltip: {
                enabled: false,
            },
        },
        yaxis: {
            labels: {
                show: false,
            },
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
        },
        responsive: [
            {
                breakpoint: 1694,
                options: {
                    chart: {
                        width: 100,
                    },
                    annotations: {
                        points: [
                            {
                                x: 75,
                                y: 58,
                                marker: {
                                    size: 4,
                                    fillColor: "#54BA4A",
                                    strokeColor: "var(--white)",
                                    radius: 2,
                                },
                            },
                        ],
                    },
                },
            },
            {
                breakpoint: 1661,
                options: {
                    chart: {
                        width: 120,
                    },
                    annotations: {
                        points: [
                            {
                                x: 90,
                                y: 58,
                                marker: {
                                    size: 4,
                                    fillColor: "#54BA4A",
                                    strokeColor: "var(--white)",
                                    radius: 2,
                                },
                            },
                        ],
                    },
                },
            },
            {
                breakpoint: 1378,
                options: {
                    chart: {
                        width: 100,
                    },
                    annotations: {
                        points: [
                            {
                                x: 75,
                                y: 58,
                                marker: {
                                    size: 4,
                                    fillColor: "#54BA4A",
                                    strokeColor: "var(--white)",
                                    radius: 2,
                                },
                            },
                        ],
                    },
                },
            },
            {
                breakpoint: 1288,
                options: {
                    chart: {
                        width: 80,
                    },
                    annotations: {
                        points: [
                            {
                                x: 50,
                                y: 58,
                                marker: {
                                    size: 4,
                                    fillColor: "#54BA4A",
                                    strokeColor: "var(--white)",
                                    radius: 2,
                                },
                            },
                        ],
                    },
                },
            },
            {
                breakpoint: 1200,
                options: {
                    chart: {
                        width: 110,
                    },
                    annotations: {
                        points: [
                            {
                                x: 85,
                                y: 58,
                                marker: {
                                    size: 4,
                                    fillColor: "#54BA4A",
                                    strokeColor: "var(--white)",
                                    radius: 2,
                                },
                            },
                        ],
                    },
                },
            },
        ],
    },
    series4: [
        {
            name: "photo",
            data: [10, 12, 41, 36, 60, 58],
        },
    ],
    options5: {
        chart: {
            width: 125,
            height: 150,
            type: "line",
            zoom: {
                enabled: false,
            },
            toolbar: {
                show: false,
            },
            dropShadow: {
                enabled: true,
                top: 8,
                left: 0,
                blur: 3,
                color: "var(--theme-secondary)",
                opacity: 0.2,
            },
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            curve: "smooth",
            width: 2,
        },
        grid: {
            show: false,
        },
        tooltip: {
            x: {
                show: false,
            },
            z: {
                show: false,
            },
        },
        colors: ["var(--theme-secondary)"],
        annotations: {
            points: [
                {
                    x: 90,
                    y: 58,
                    marker: {
                        size: 4,
                        fillColor: "var(--theme-secondary)",
                        strokeColor: "var(--white)",
                        radius: 2,
                    },
                },
            ],
        },
        fill: {
            opacity: 1,
            type: "gradient",
            gradient: {
                shade: "light",
                type: "vertical",
                shadeIntensity: 1,
                opacityFrom: 0.95,
                opacityTo: 1,
                colorStops: [
                    {
                        offset: 0,
                        color: "var(--theme-secondary)",
                        opacity: 0.1,
                    },
                    {
                        offset: 30,
                        color: "var(--theme-secondary)",
                        opacity: 0.8,
                    },
                    {
                        offset: 80,
                        color: "var(--theme-secondary)",
                        opacity: 1,
                    },
                    {
                        offset: 100,
                        color: "var(--theme-secondary)",
                        opacity: 0.1,
                    },
                ],
            },
        },
        xaxis: {
            categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            labels: {
                show: false,
            },
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
            tooltip: {
                enabled: false,
            },
        },
        yaxis: {
            labels: {
                show: false,
            },
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
        },
        responsive: [
            {
                breakpoint: 1694,
                options: {
                    chart: {
                        width: 100,
                    },
                    annotations: {
                        points: [
                            {
                                x: 75,
                                y: 58,
                                marker: {
                                    size: 4,
                                    fillColor: "var(--theme-secondary)",
                                    strokeColor: "var(--white)",
                                    radius: 2,
                                },
                            },
                        ],
                    },
                },
            },
            {
                breakpoint: 1661,
                options: {
                    chart: {
                        width: 120,
                    },
                    annotations: {
                        points: [
                            {
                                x: 90,
                                y: 58,
                                marker: {
                                    size: 4,
                                    fillColor: "var(--theme-secondary)",
                                    strokeColor: "var(--white)",
                                    radius: 2,
                                },
                            },
                        ],
                    },
                },
            },
            {
                breakpoint: 1378,
                options: {
                    chart: {
                        width: 100,
                    },
                    annotations: {
                        points: [
                            {
                                x: 75,
                                y: 58,
                                marker: {
                                    size: 4,
                                    fillColor: "var(--theme-secondary)",
                                    strokeColor: "var(--white)",
                                    radius: 2,
                                },
                            },
                        ],
                    },
                },
            },
            {
                breakpoint: 1288,
                options: {
                    chart: {
                        width: 80,
                    },
                    annotations: {
                        points: [
                            {
                                x: 50,
                                y: 58,
                                marker: {
                                    size: 4,
                                    fillColor: "var(--theme-secondary)",
                                    strokeColor: "var(--white)",
                                    radius: 2,
                                },
                            },
                        ],
                    },
                },
            },
            {
                breakpoint: 1200,
                options: {
                    chart: {
                        width: 110,
                    },
                    annotations: {
                        points: [
                            {
                                x: 85,
                                y: 58,
                                marker: {
                                    size: 4,
                                    fillColor: "var(--theme-secondary)",
                                    strokeColor: "var(--white)",
                                    radius: 2,
                                },
                            },
                        ],
                    },
                },
            },
        ],
    },
    series5: [
        {
            name: "photo",
            data: [10, 12, 41, 36, 60, 58],
        },
    ],
    options6: {
        chart: {
            width: 325,
            height: 325,
            type: "radialBar",
            dropShadow: {
                enabled: true,
                top: 5,
                left: 8,
                blur: 8,
                color: "var(--theme-deafult)",
                opacity: 0.2,
            },
        },
        plotOptions: {
            radialBar: {
                hollow: {
                    margin: 5,
                    size: "70%",
                    image: "/images/dashboard-5/follower.png",
                    imageWidth: 50,
                    imageHeight: 50,
                    imageClipped: false,
                },
                track: {
                    background: "transparent",
                },
            },
        },
        colors: ["var(--theme-deafult)", "#FFA941"],
        labels: ["Male", "Female"],
        stroke: {
            lineCap: "round",
        },
        legend: {
            show: true,
            position: "right",
            horizontalAlign: "center",
            offsetY: -15,
            fontSize: "14px",
            fontFamily: "Rubik, sans-serif",
            fontWeight: 500,
            labels: {
                colors: "var(--chart-text-color)",
            },
            markers: {
                width: 6,
                height: 6,
            },
        },
        responsive: [
            {
                breakpoint: 718,
                options: {
                    chart: {
                        width: "100%",
                        height: 230,
                    },
                    legend: {
                        show: false,
                    },
                },
            },
        ],
    },
    series6: [70, 60],
    options7: {
        chart: {
            height: 305,
            type: "line",
            zoom: {
                enabled: false,
            },
            toolbar: {
                show: false,
            },
            dropShadow: {
                enabled: true,
                top: 8,
                left: 0,
                blur: 3,
                color: "var(--theme-deafult)",
                opacity: 0.2,
            },
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            curve: "smooth",
            width: 3,
        },
        grid: {
            row: {
                colors: ["var(--view-grid-bg)", "transparent"],
                opacity: 0.5,
            },
            column: {
                colors: ["var(--view-grid-bg)", "transparent"],
            },
            xaxis: {
                lines: {
                    show: true,
                },
            },
        },

        tooltip: {
            x: {
                show: false,
            },
            z: {
                show: false,
            },
        },
        colors: ["var(--theme-deafult)"],
        fill: {
            opacity: 1,
            type: "gradient",
            gradient: {
                shade: "light",
                type: "vertical",
                shadeIntensity: 1,
                opacityFrom: 0.95,
                opacityTo: 1,
                colorStops: [
                    {
                        offset: 0,
                        color: "var(--theme-deafult)",
                        opacity: 0.05,
                    },
                    {
                        offset: 30,
                        color: "var(--theme-deafult)",
                        opacity: 1,
                    },
                    {
                        offset: 80,
                        color: "var(--theme-deafult)",
                        opacity: 1,
                    },
                    {
                        offset: 100,
                        color: "var(--theme-deafult)",
                        opacity: 0.1,
                    },
                ],
            },
        },
        annotations: {
            points: [
                {
                    x: "Feb",
                    y: 44,
                    marker: {
                        size: 15,
                        fillColor: "#7366FF",
                        strokeColor: "var(--view-border-marker)",
                        strokeWidth: 20,
                        radius: 2,
                        cssClass: "apexcharts-custom-class",
                    },
                },
            ],
        },
        xaxis: {
            categories: ["Jan", "Feb", "Mar", "Apr"],
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
            tooltip: {
                enabled: false,
            },
        },
        yaxis: {
            axisBorder: {
                show: false,
            },
            axisTicks: {
                show: false,
            },
        },
        responsive: [
            {
                breakpoint: 768,
                options: {
                    chart: {
                        height: 200,
                    },
                },
            },
            {
                breakpoint: 481,
                options: {
                    annotations: {
                        points: [
                            {
                                x: "Feb",
                                y: 44,
                                marker: {
                                    size: 10,
                                    fillColor: "#7366FF",
                                    strokeColor: "#cfcdfc",
                                    strokeWidth: 7,
                                    radius: 2,
                                    cssClass: "apexcharts-custom-class",
                                },
                            },
                        ],
                    },
                },
            },
        ],
    },
    series7: [
        {
            name: "view",
            data: [20, 45, 30, 50],
        },
    ],
    options8: {
        chart: {
            height: 130,
            type: "radialBar",
            dropShadow: {
                enabled: true,
                top: 3,
                left: 0,
                blur: 10,
                color: "#FF3364",
                opacity: 0.35,
            },
        },
        plotOptions: {
            radialBar: {
                hollow: {
                    size: "60%",
                },
                track: {
                    strokeWidth: "60%",
                    opacity: 1,
                    margin: 5,
                },
                dataLabels: {
                    showOn: "always",
                    value: {
                        color: "var(--body-font-color)",
                        fontSize: "14px",
                        show: true,
                        offsetY: -10,
                    },
                },
            },
        },
        colors: ["#FF3364"],
        stroke: {
            lineCap: "round",
        },
        responsive: [
            {
                breakpoint: 1500,
                options: {
                    chart: {
                        height: 130,
                    },
                },
            },
        ],
    },
    series8: [80],
};
export const chart = {
    chart1: {
        options: {
            chart: {
                width: 510,
                height: 190,
                type: "area",
                toolbar: {
                    show: false,
                },
            },
            colors: [primary],
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
                width: 2,
            },
            xaxis: {
                show: false,
                type: "datetime",
                categories: [
                    "2018-09-19T00:00:00",
                    "2018-09-19T01:30:00",
                    "2018-09-19T02:30:00",
                    "2018-09-19T03:30:00",
                    "2018-09-19T04:30:00",
                    "2018-09-19T05:30:00",
                    "2018-09-19T06:30:00",
                    "2018-09-19T07:30:00",
                    "2018-09-19T08:30:00",
                    "2018-09-19T09:30:00",
                ],
                labels: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
            },
            yaxis: {
                show: false,
            },
            fill: {
                colors: [primary],
            },
            tooltip: {
                x: {
                    format: "dd/MM/yy HH:mm",
                },
            },
            grid: {
                show: false,
                padding: {
                    left: 0,
                    right: -10,
                    bottom: -50,
                },
            },
        },
        series: [
            {
                name: "series1",
                data: [14, 12, 20, 20, 14, 22, 18, 26, 12, 18, 0],
            },
        ],
    },
    chart2: {
        options: {
            chart: {
                width: 510,
                height: 190,
                type: "area",
                toolbar: {
                    show: false,
                },
            },
            colors: [secondary],
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
                width: 2,
            },
            xaxis: {
                show: false,
                type: "datetime",
                categories: [
                    "2018-09-19T00:00:00",
                    "2018-09-19T01:30:00",
                    "2018-09-19T02:30:00",
                    "2018-09-19T03:30:00",
                    "2018-09-19T04:30:00",
                    "2018-09-19T05:30:00",
                    "2018-09-19T06:30:00",
                    "2018-09-19T07:30:00",
                    "2018-09-19T08:30:00",
                    "2018-09-19T09:30:00",
                ],
                labels: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
            },
            yaxis: {
                show: false,
            },
            fill: {
                colors: [secondary],
            },
            tooltip: {
                x: {
                    format: "dd/MM/yy HH:mm",
                },
            },
            grid: {
                show: false,
                padding: {
                    left: 0,
                    right: -10,
                    bottom: -50,
                },
            },
        },
        series: [
            {
                name: "series1",
                data: [14, 12, 20, 20, 14, 22, 18, 26, 12, 18, 0],
            },
        ],
    },
    chart3: {
        options: {
            chart: {
                width: 510,
                height: 190,
                type: "area",
                toolbar: {
                    show: false,
                },
            },
            colors: ["#51BB25"],
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
                width: 2,
            },
            xaxis: {
                show: false,
                type: "datetime",
                categories: [
                    "2018-09-19T00:00:00",
                    "2018-09-19T01:30:00",
                    "2018-09-19T02:30:00",
                    "2018-09-19T03:30:00",
                    "2018-09-19T04:30:00",
                    "2018-09-19T05:30:00",
                    "2018-09-19T06:30:00",
                    "2018-09-19T07:30:00",
                    "2018-09-19T08:30:00",
                    "2018-09-19T09:30:00",
                ],
                labels: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
            },
            yaxis: {
                show: false,
            },
            fill: {
                colors: ["#51BB25"],
            },
            tooltip: {
                x: {
                    format: "dd/MM/yy HH:mm",
                },
            },
            grid: {
                show: false,
                padding: {
                    left: 0,
                    right: -10,
                    bottom: -50,
                },
            },
        },
        series: [
            {
                name: "series1",
                data: [14, 12, 20, 20, 14, 22, 18, 26, 12, 18, 0],
            },
        ],
    },
    chart4: {
        options: {
            chart: {
                width: 855,
                height: 350,
                type: "bar",
                toolbar: {
                    show: false,
                },
            },
            legend: {
                show: true,
            },
            colors: [primary, secondary],
            dataLabels: {
                enabled: false,
            },
            plotOptions: {
                bar: {
                    endingShape: "rounded",
                    radius: 10,
                    borderRadius: 8,
                    horizontal: false,
                    columnWidth: "30%",
                },
            },
            stroke: {
                show: true,
                colors: ["transparent"],
                curve: "smooth",
                lineCap: "butt",
            },
            xaxis: {
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                ],
            },
            yaxis: {
                title: {
                    text: "$ (thousands)",
                },
            },
            fill: {
                colors: [secondary, "#51bb25", primary],
            },
            tooltip: {
                y: {
                    formatter: function (val) {
                        return "$ " + val + " thousands";
                    },
                },
            },
            grid: {
                yaxis: {
                    show: false,
                },
                padding: {
                    left: 0,
                    right: 0,
                },
            },
        },
        series: [
            {
                name: "Profit",
                data: [100, 45, 30, 56, 45, 53, 41],
            },
            {
                name: "Revenue",
                data: [75, 20, 40, 52, 50, 114, 94],
            },
            {
                name: "Cash Flow",
                data: [95, 55, 100, 48, 105, 60, 66],
            },
        ],
    },
    chart5: {
        options: {
            chart: {
                width: 585,
                height: 360,
                type: "radialBar",
            },
            plotOptions: {
                radialBar: {
                    startAngle: -135,
                    endAngle: 225,
                    hollow: {
                        margin: 0,
                        size: "70%",
                        background: "#fff",
                        image: undefined,
                        imageOffsetX: 0,
                        imageOffsetY: 0,
                        position: "front",
                        dropShadow: {
                            enabled: true,
                            top: 3,
                            left: 0,
                            blur: 4,
                            opacity: 0.05,
                        },
                    },
                    track: {
                        background: "#fff",
                        strokeWidth: "67%",
                        margin: 0,
                        dropShadow: {
                            enabled: true,
                            top: -3,
                            left: 0,
                            blur: 4,
                            opacity: 0.15,
                        },
                    },
                    dataLabels: {
                        show: true,
                        name: {
                            offsetY: -10,
                            show: true,
                            color: "#111",
                            fontSize: "17px",
                        },
                        value: {
                            formatter: function (val) {
                                return parseInt(val);
                            },
                            color: "#111",
                            fontSize: "36px",
                            show: true,
                        },
                    },
                },
            },
            fill: {
                type: "gradient",
                gradient: {
                    shade: "dark",
                    type: "horizontal",
                    shadeIntensity: 0.5,
                    gradientToColors: [primary],
                    inverseColors: true,
                    opacityFrom: 1,
                    opacityTo: 1,
                    stops: [0, 100],
                },
            },
            stroke: {
                lineCap: "round",
            },
        },
        series: [70],
        labels: ["Volatility"],
    },
    chart6: {
        options: {
            chart: {
                width: 450,
                height: 350,
                type: "radialBar",
                offsetY: -30,
                offsetX: 20,
            },
            legend: {
                show: true,
            },
            colors: [secondary, primary, "#51bb25"],
            plotOptions: {
                radialBar: {
                    size: undefined,
                    inverseOrder: false,
                    hollow: {
                        margin: 5,
                        size: "48%",
                        background: "transparent",
                    },
                    track: {
                        show: true,
                        background: "#f2f2f2",
                        strokeWidth: "10%",
                        opacity: 1,
                        margin: 3,
                    },
                },
            },
        },
        series: [75, 63, 50],
        labels: ["Skill 01", "Skill 02", "Skill 03"],
    },
    progress1: {
        options: {
            chart: {
                fontFamily: "Roboto, sans-serif",
                width: 990,
                height: 70,
                type: "bar",
                stacked: true,
                sparkline: {
                    enabled: true,
                },
            },
            stroke: {
                width: 0,
            },
            fill: {
                colors: ["rgba(115, 102, 255, 1)"],
            },
            legend: {
                show: true,
            },
            colors: ["rgba(115, 102, 255, 1)"],
            plotOptions: {
                bar: {
                    horizontal: true,
                    barHeight: "10%",
                    colors: {
                        backgroundBarColors: ["rgba(115, 102, 255, 0.1)"],
                    },
                },
            },
            title: {
                floating: true,
                offsetX: -10,
                offsetY: 5,
                text: "Packed",
            },
            subtitle: {
                floating: true,
                align: "right",
                offsetY: 0,
                text: "20%",
            },
            tooltip: {
                enabled: false,
            },
            xaxis: {
                categories: ["Process 1"],
            },
            yaxis: {
                max: 100,
            },
        },
        series: [
            {
                name: "Process 1",
                data: [20],
            },
        ],
        labels: ["Device 1", "Device 2"],
    },
    progress2: {
        options: {
            chart: {
                fontFamily: "Roboto, sans-serif",
                width: 990,
                height: 70,
                type: "bar",
                stacked: true,
                sparkline: {
                    enabled: true,
                },
            },
            stroke: {
                lineCap: "round",
            },
            fill: {
                colors: ["#f73164"],
            },
            legend: {
                show: true,
            },
            colors: ["#f73164"],
            plotOptions: {
                bar: {
                    horizontal: true,
                    barHeight: "10%",
                    colors: {
                        backgroundBarColors: ["rgba(249 ,79 ,123, 0.1)"],
                    },
                },
            },
            title: {
                floating: true,
                offsetX: -10,
                offsetY: 5,
                text: "Dispatched",
            },
            subtitle: {
                floating: true,
                align: "right",
                offsetY: 0,
                text: "40%",
            },
            tooltip: {
                enabled: false,
            },
            xaxis: {
                categories: ["Process 2"],
            },
            yaxis: {
                max: 100,
            },
        },
        series: [
            {
                name: "Process 2",
                data: [40],
            },
        ],
        labels: ["Device 1", "Device 2"],
    },
    progress3: {
        options: {
            chart: {
                fontFamily: "Roboto, sans-serif",
                width: 990,
                height: 70,
                type: "bar",
                stacked: true,
                sparkline: {
                    enabled: true,
                },
            },
            stroke: {
                width: 0,
            },
            fill: {
                colors: ["#a927f9"],
            },
            legend: {
                show: true,
            },
            colors: ["#a927f9"],
            plotOptions: {
                bar: {
                    horizontal: true,
                    barHeight: "10%",
                    colors: {
                        backgroundBarColors: ["rgba(180, 74, 248, 0.1)"],
                    },
                },
            },
            title: {
                floating: true,
                offsetX: -10,
                offsetY: 5,
                text: "Reach Station",
            },
            subtitle: {
                floating: true,
                align: "right",
                offsetY: 0,
                text: "50%",
            },
            tooltip: {
                enabled: false,
            },
            xaxis: {
                categories: ["Process 3"],
            },
            yaxis: {
                max: 100,
            },
        },
        series: [
            {
                name: "Process 3",
                data: [50],
            },
        ],
        labels: ["Device 1", "Device 2"],
    },
    progress4: {
        options: {
            chart: {
                fontFamily: "Roboto, sans-serif",
                width: 990,
                height: 70,
                type: "bar",
                stacked: true,
                sparkline: {
                    enabled: true,
                },
            },
            stroke: {
                width: 0,
            },
            fill: {
                colors: ["#F8D62B"],
            },
            legend: {
                show: true,
            },
            colors: ["#F8D62B"],
            plotOptions: {
                bar: {
                    horizontal: true,
                    barHeight: "10%",
                    colors: {
                        backgroundBarColors: ["rgba(248,214, 43, 0.1)"],
                    },
                },
            },
            title: {
                floating: true,
                offsetX: -10,
                offsetY: 5,
                text: "Out for delivery",
            },
            subtitle: {
                floating: true,
                align: "right",
                offsetY: 0,
                text: "60%",
            },
            tooltip: {
                enabled: false,
            },
            xaxis: {
                categories: ["Process 4"],
            },
            yaxis: {
                max: 100,
            },
        },
        series: [
            {
                name: "Process 4",
                data: [60],
            },
        ],
        labels: ["Device 1", "Device 2"],
    },
    progress5: {
        options: {
            chart: {
                fontFamily: "Roboto, sans-serif",
                width: 990,
                height: 70,
                type: "bar",
                stacked: true,
                sparkline: {
                    enabled: true,
                },
            },
            stroke: {
                width: 0,
            },
            fill: {
                colors: ["#51bb25"],
            },
            legend: {
                show: true,
            },
            colors: ["#51bb25"],
            plotOptions: {
                bar: {
                    horizontal: true,
                    barHeight: "10%",
                    colors: {
                        backgroundBarColors: ["rgba(107, 197, 75, 0.1)"],
                    },
                },
            },
            title: {
                floating: true,
                offsetX: -10,
                offsetY: 5,
                text: "Delivered",
            },
            subtitle: {
                floating: true,
                align: "right",
                offsetY: 0,
                text: "10%",
            },
            tooltip: {
                enabled: false,
            },
            xaxis: {
                categories: ["Process 5"],
            },
            yaxis: {
                max: 100,
            },
        },
        series: [
            {
                name: "Process 5",
                data: [10],
            },
        ],
        labels: ["Device 1", "Device 2"],
    },
    chart7: {
        options: {
            chart: {
                width: 585,
                height: 350,
                type: "bar",
                toolbar: {
                    show: false,
                },
                zoom: {
                    enabled: false,
                },
            },
            legend: {
                show: false,
            },
            colors: [primary],
            dataLabels: {
                enabled: false,
            },
            plotOptions: {
                bar: {
                    radius: 10,
                    horizontal: false,
                    columnWidth: "55%",
                },
            },
            stroke: {
                show: true,
                colors: ["transparent"],
                curve: "smooth",
                lineCap: "butt",
            },
            title: {
                text: "Load Average",
                align: "left",
                style: {
                    fontSize: "12px",
                },
            },
            subtitle: {
                text: "20%",
                floating: true,
                align: "right",
                offsetY: 0,
                style: {
                    fontSize: "22px",
                },
            },
            xaxis: {
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
            },
            fill: {
                colors: [primary],
            },
            tooltip: {
                y: {
                    formatter: function (val) {
                        return "$ " + val + " thousands";
                    },
                },
            },
        },
        series: [
            {
                data: [200, 250, 330, 390, 420, 500, 580, 620, 700],
            },
        ],
    },
    chart8: {
        options: {
            chart: {
                height: 350,
                type: "line",
                toolbar: {
                    show: false,
                },
            },
            dataLabels: {
                enabled: false,
            },
            colors: [secondary, primary],
            title: {
                text: "HeatMap Chart",
            },
        },
        stroke: {
            width: [2, 2],
        },
        series: [
            {
                name: "Complete",
                data: [35, 45, 20, 42, 48, 35, 55, 60, 45, 65, 58, 62],
            },
            {
                name: "Running",
                data: [35, 55, 50, 60, 75, 65, 64, 80, 90, 80, 83, 90],
            },
        ],
    },
    candleChart9: {
        options: {
            chart: {
                width: 1530,
                height: 500,
                type: "candlestick",
                toolbar: {
                    show: false,
                },
            },
            plotOptions: {
                candlestick: {
                    colors: {
                        upward: primary,
                        downward: secondary,
                    },
                },
            },
            colors: [primary],
            title: {
                text: "CandleStick Chart",
                align: "left",
            },
            xaxis: {
                type: "datetime",
            },
            yaxis: {
                tooltip: {
                    enabled: true,
                },
            },
        },
        series: [
            {
                data: [
                    {
                        x: new Date(1538778600000),
                        y: [6629.81, 6650.5, 6623.04, 6633.33],
                    },
                    {
                        x: new Date(1538780400000),
                        y: [6632.01, 6643.59, 6620, 6630.11],
                    },
                    {
                        x: new Date(1538782200000),
                        y: [6630.71, 6648.95, 6623.34, 6635.65],
                    },
                    {
                        x: new Date(1538784000000),
                        y: [6635.65, 6651, 6629.67, 6638.24],
                    },
                    {
                        x: new Date(1538785800000),
                        y: [6638.24, 6640, 6620, 6624.47],
                    },
                    {
                        x: new Date(1538787600000),
                        y: [6624.53, 6636.03, 6621.68, 6624.31],
                    },
                    {
                        x: new Date(1538789400000),
                        y: [6624.61, 6632.2, 6617, 6626.02],
                    },
                    {
                        x: new Date(1538791200000),
                        y: [6627, 6627.62, 6584.22, 6603.02],
                    },
                    {
                        x: new Date(1538793000000),
                        y: [6605, 6608.03, 6598.95, 6604.01],
                    },
                    {
                        x: new Date(1538794800000),
                        y: [6604.5, 6614.4, 6602.26, 6608.02],
                    },
                    {
                        x: new Date(1538796600000),
                        y: [6608.02, 6610.68, 6601.99, 6608.91],
                    },
                    {
                        x: new Date(1538798400000),
                        y: [6608.91, 6618.99, 6608.01, 6612],
                    },
                    {
                        x: new Date(1538800200000),
                        y: [6612, 6615.13, 6605.09, 6612],
                    },
                    {
                        x: new Date(1538802000000),
                        y: [6612, 6624.12, 6608.43, 6622.95],
                    },
                    {
                        x: new Date(1538803800000),
                        y: [6623.91, 6623.91, 6615, 6615.67],
                    },
                    {
                        x: new Date(1538805600000),
                        y: [6618.69, 6618.74, 6610, 6610.4],
                    },
                    {
                        x: new Date(1538807400000),
                        y: [6611, 6622.78, 6610.4, 6614.9],
                    },
                    {
                        x: new Date(1538809200000),
                        y: [6614.9, 6626.2, 6613.33, 6623.45],
                    },
                    {
                        x: new Date(1538811000000),
                        y: [6623.48, 6627, 6618.38, 6620.35],
                    },
                    {
                        x: new Date(1538812800000),
                        y: [6619.43, 6620.35, 6610.05, 6615.53],
                    },
                    {
                        x: new Date(1538814600000),
                        y: [6615.53, 6617.93, 6610, 6615.19],
                    },
                    {
                        x: new Date(1538816400000),
                        y: [6615.19, 6621.6, 6608.2, 6620],
                    },
                    {
                        x: new Date(1538818200000),
                        y: [6619.54, 6625.17, 6614.15, 6620],
                    },
                    {
                        x: new Date(1538820000000),
                        y: [6620.33, 6634.15, 6617.24, 6624.61],
                    },
                    {
                        x: new Date(1538821800000),
                        y: [6625.95, 6626, 6611.66, 6617.58],
                    },
                    {
                        x: new Date(1538823600000),
                        y: [6619, 6625.97, 6595.27, 6598.86],
                    },
                    {
                        x: new Date(1538825400000),
                        y: [6598.86, 6598.88, 6570, 6587.16],
                    },
                    {
                        x: new Date(1538827200000),
                        y: [6588.86, 6600, 6580, 6593.4],
                    },
                    {
                        x: new Date(1538829000000),
                        y: [6593.99, 6598.89, 6585, 6587.81],
                    },
                    {
                        x: new Date(1538830800000),
                        y: [6587.81, 6592.73, 6567.14, 6578],
                    },
                    {
                        x: new Date(1538832600000),
                        y: [6578.35, 6581.72, 6567.39, 6579],
                    },
                    {
                        x: new Date(1538834400000),
                        y: [6579.38, 6580.92, 6566.77, 6575.96],
                    },
                    {
                        x: new Date(1538836200000),
                        y: [6575.96, 6589, 6571.77, 6588.92],
                    },
                    {
                        x: new Date(1538838000000),
                        y: [6588.92, 6594, 6577.55, 6589.22],
                    },
                    {
                        x: new Date(1538839800000),
                        y: [6589.3, 6598.89, 6589.1, 6596.08],
                    },
                    {
                        x: new Date(1538841600000),
                        y: [6597.5, 6600, 6588.39, 6596.25],
                    },
                    {
                        x: new Date(1538843400000),
                        y: [6598.03, 6600, 6588.73, 6595.97],
                    },
                    {
                        x: new Date(1538845200000),
                        y: [6595.97, 6602.01, 6588.17, 6602],
                    },
                    {
                        x: new Date(1538847000000),
                        y: [6602, 6607, 6596.51, 6599.95],
                    },
                    {
                        x: new Date(1538848800000),
                        y: [6600.63, 6601.21, 6590.39, 6591.02],
                    },
                    {
                        x: new Date(1538850600000),
                        y: [6591.02, 6603.08, 6591, 6591],
                    },
                    {
                        x: new Date(1538852400000),
                        y: [6591, 6601.32, 6585, 6592],
                    },
                    {
                        x: new Date(1538854200000),
                        y: [6593.13, 6596.01, 6590, 6593.34],
                    },
                    {
                        x: new Date(1538856000000),
                        y: [6593.34, 6604.76, 6582.63, 6593.86],
                    },
                    {
                        x: new Date(1538857800000),
                        y: [6593.86, 6604.28, 6586.57, 6600.01],
                    },
                    {
                        x: new Date(1538859600000),
                        y: [6601.81, 6603.21, 6592.78, 6596.25],
                    },
                    {
                        x: new Date(1538861400000),
                        y: [6596.25, 6604.2, 6590, 6602.99],
                    },
                    {
                        x: new Date(1538863200000),
                        y: [6602.99, 6606, 6584.99, 6587.81],
                    },
                    {
                        x: new Date(1538865000000),
                        y: [6587.81, 6595, 6583.27, 6591.96],
                    },
                    {
                        x: new Date(1538866800000),
                        y: [6591.97, 6596.07, 6585, 6588.39],
                    },
                    {
                        x: new Date(1538868600000),
                        y: [6587.6, 6598.21, 6587.6, 6594.27],
                    },
                    {
                        x: new Date(1538870400000),
                        y: [6596.44, 6601, 6590, 6596.55],
                    },
                    {
                        x: new Date(1538872200000),
                        y: [6598.91, 6605, 6596.61, 6600.02],
                    },
                    {
                        x: new Date(1538874000000),
                        y: [6600.55, 6605, 6589.14, 6593.01],
                    },
                    {
                        x: new Date(1538875800000),
                        y: [6593.15, 6605, 6592, 6603.06],
                    },
                    {
                        x: new Date(1538877600000),
                        y: [6603.07, 6604.5, 6599.09, 6603.89],
                    },
                    {
                        x: new Date(1538879400000),
                        y: [6604.44, 6604.44, 6600, 6603.5],
                    },
                    {
                        x: new Date(1538881200000),
                        y: [6603.5, 6603.99, 6597.5, 6603.86],
                    },
                    {
                        x: new Date(1538883000000),
                        y: [6603.85, 6605, 6600, 6604.07],
                    },
                    {
                        x: new Date(1538884800000),
                        y: [6604.98, 6606, 6604.07, 6606],
                    },
                ],
            },
        ],
    },
    chart10: {
        options: {
            chart: {
                width: 855,
                height: 320,
                type: "line",
                toolbar: {
                    show: false,
                },
            },
            colors: [primary, secondary],
            stroke: {
                curve: "smooth",
                width: 0,
            },
            markers: {
                size: 0,
            },
            yaxis: [
                {
                    title: {
                        text: "Dollars in thounand",
                    },
                },
            ],
            fill: {
                colors: [secondary, primary],
                opacity: 0.5,
            },
            tooltip: {
                shared: true,
            },
        },
        labels: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
        ],
        series: [
            {
                name: "TEAM A",
                type: "area",
                data: [60, 90, 65, 80, 55, 72, 30, 50, 31],
            },
            {
                name: "TEAM B",
                type: "area",
                data: [20, 30, 25, 50, 32, 75, 65, 80, 45],
            },
        ],
    },
    chart11: {
        options: {
            chart: {
                width: 510,
                height: 190,
                type: "area",
                toolbar: {
                    show: false,
                },
            },
            colors: [primary],
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
                width: 2,
            },
            xaxis: {
                show: true,
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                ],
            },
            fill: {
                colors: [primary],
            },
            tooltip: {
                x: {
                    format: "dd/MM/yy HH:mm",
                },
            },
            grid: {
                yaxis: {
                    show: false,
                },
                padding: {
                    right: -75,
                    bottom: 0,
                },
            },
        },
        series: [
            {
                data: [14, 12, 20, 20, 14, 22, 18, 26, 12],
            },
        ],
    },
    chart12: {
        options: {
            chart: {
                toolbar: {
                    show: false,
                },
                height: 400,
                type: "area",
            },
            dataLabels: {
                enabled: false,
            },
            stroke: {
                width: 3,
                curve: "smooth",
            },
            xaxis: {
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                ],
                tickAmount: 5,
                tickPlacement: "between",
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                tooltip: {
                    enabled: false,
                },
            },
            grid: {
                borderColor: "rgba(196,196,196, 0.3)",
                padding: {
                    top: -20,
                    right: -16,
                    bottom: 0,
                },
            },
            fill: {
                opacity: 0.2,
            },
            colors: [primary],

            tooltip: {
                x: {
                    format: "dd/MM/yy HH:mm",
                },
            },
            responsive: [
                {
                    breakpoint: 576,
                    options: {
                        chart: {
                            height: 200,
                        },
                    },
                },
            ],
        },
        series: [
            {
                data: [
                    20, 120, 15, 100, 120, 60, 150, 70, 100, 80, 105, 20, 70,
                    60, 10, 12, 10, 130, 60, 80, 40, 140, 110, 150, 30, 75, 20,
                    45, 15, 130, 10, 30, 15, 110, 65, 130, 0,
                ],
            },
        ],
    },
    chart13: {
        options: {
            chart: {
                height: 400,
                type: "line",
                toolbar: {
                    show: false,
                },
            },
            annotations: {
                yaxis: [
                    {
                        y: 8200,
                        y2: 8400,
                        borderColor: "#f8d62b",
                        fillColor: "#f8d62b",
                        opacity: 0.1,
                        label: {
                            borderColor: "#f8d62b",
                            offsetX: -30,
                            style: {
                                fontSize: "10px",
                                color: "#fff",
                                background: "#f8d62b",
                            },
                            text: "Y-axis range",
                        },
                    },
                ],
                xaxis: [
                    {
                        x: new Date("15 Nov 2017").getTime(),
                        strokeDashArray: 0,
                        borderColor: primary,
                        label: {
                            borderColor: primary,
                            offsetY: 20,
                            style: {
                                color: "#fff",
                                background: primary,
                            },
                            text: "Anno Test",
                        },
                    },
                    {
                        x: new Date("17 Nov 2017").getTime(),
                        x2: new Date("18 Nov 2017").getTime(),
                        fillColor: "#51bb25",
                        opacity: 0.1,
                        label: {
                            borderColor: "##51bb25",
                            style: {
                                fontSize: "10px",
                                color: "#fff",
                                background: "#51bb25",
                            },
                            offsetY: 20,
                            text: "X-axis range",
                        },
                    },
                ],
            },
            dataLabels: {
                enabled: false,
            },
            stroke: {
                width: 3,
                curve: "smooth",
            },
            grid: {
                padding: {
                    right: 30,
                    left: 20,
                },
            },
            title: {
                text: "Line with Annotations",
                align: "left",
                style: {
                    fontSize: "18px",
                    fontFamily: "Rubik, sans-serif",
                    fontWeight: 500,
                },
            },
            colors: [secondary],
            labels: series.monthDataSeries1.dates,
            xaxis: {
                type: "datetime",
            },
            responsive: [
                {
                    breakpoint: 576,
                    options: {
                        title: {
                            style: {
                                fontSize: "16px",
                            },
                        },
                    },
                },
            ],
        },
        series: [
            {
                data: series.monthDataSeries1.prices,
            },
        ],
    },
    chart14: {
        options: {
            fill: {
                type: "gradient",
                gradient: {
                    shade: "light",
                    type: "Reflected",
                    shadeIntensity: 0.1,
                    inverseColors: false,
                    opacityFrom: 1,
                    opacityTo: 0.8,
                    stops: [0, 100],
                },
            },
            colors: [primary, secondary, "#544fff"],
            chart: {
                height: 300,
                type: "radar",
                dropShadow: {
                    enabled: true,
                    blur: 1,
                    left: 1,
                    top: 1,
                },
            },
            title: {
                text: "Radar Chart - Multi Series",
            },
            stroke: {
                width: 0,
            },
            markers: {
                size: 0,
            },
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        },
        series: [
            {
                name: "Series 1",
                data: [80, 50, 30, 40, 99, 20],
            },
            {
                name: "Series 2",
                data: [20, 30, 40, 80, 20, 80],
            },
            {
                name: "Series 3",
                data: [44, 76, 78, 13, 43, 10],
            },
        ],
    },
    chart15: {
        options: {
            chart: {
                toolbar: {
                    show: false,
                },
            },
            dataLabels: {
                enabled: false,
            },
            fill: {
                type: "gradient",
                gradient: {
                    shade: "light",
                    type: "horizontal",
                    shadeIntensity: 0.4,
                    inverseColors: false,
                    opacityFrom: 1,
                    opacityTo: 0.7,
                    stops: [0, 100],
                },
            },
            colors: [primary, secondary, "#51bb25", "#544fff"],
            title: {
                text: "Simple Bubble Chart",
            },
            xaxis: {
                show: false,
                labels: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                max: 70,
            },
        },
        series: [
            {
                name: "Bubble1",
                data: generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
                    min: 10,
                    max: 60,
                }),
            },
            {
                name: "Bubble2",
                data: generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
                    min: 10,
                    max: 60,
                }),
            },
            {
                name: "Bubble3",
                data: generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
                    min: 10,
                    max: 60,
                }),
            },
            {
                name: "Bubble4",
                data: generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
                    min: 10,
                    max: 60,
                }),
            },
        ],
    },
};
