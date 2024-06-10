 import products from '@/data/product.json';
 import productswiper from "@/data/productswiper.json"
 export const useProductStore = defineStore({
	id: 'Product',
	state:()=>{
		return{
			products: products.data,
			swiper:productswiper.swiper,
	swiper1:productswiper.swiper1,
			// productslist: products.data,
			// cart: JSON.parse(localStorage.getItem('cartItem')) || cartItems,
			cart: cartItems,
			order: [],
			tagItems: [],
			filteredProduct: [],
			searchTerm: '',
			column2: false,  
			column3: false,
			column4: true,
			column6: false,
			listViewEnabled: false,
			list: false,
			price: [],
		}
	},
	getters:{
		price:(state)=>{
			return state.products.map((product) => {
				if(product.price){
					return product.price
				}
			})
			
		},
		col2:(state)=>{
			return state.column2 
		  },
		col3:(state)=>{
			return state.column3
		},
		col4:(state)=>{
			return state.column4
		},
		col6:(state)=>{
			return state.column6
		},
		listViewEnable:(state)=>{
			return state.listViewEnabled
		},
		 
		getTotalAmount: (state) => {
			return state.cart.reduce((prev, curr) => {
				return prev + curr.price * curr.quantity;
			}, 0);
		},
		getBrands: (state) => {
			const brands = [...new Set(state.products.map(product => product.brand))];
			return brands;
		},
		getCategory: (state) => {
			var uniqueCategory = [];
			var itemCat = Array();
			state.products.map((product) => {
				if (product.category) {
					product.category.map((category) => {
						const index = uniqueCategory.indexOf(category);
						if (index === -1) uniqueCategory.push(category);
					});
				}
			});
			for (var i = 0; i < uniqueCategory.length; i++) {
				itemCat.push({ category: uniqueCategory[i] });
			}
			return itemCat;
		},
		getColors: (state) => {
			var uniqueColors = [];
			var itemColor = Array();
			state.products.map((product) => {
				if (product.colors) {
					product.colors.map((color) => {
						const index = uniqueColors.indexOf(color);
						if (index === -1) uniqueColors.push(color);
					});
				}
			});
			for (var i = 0; i < uniqueColors.length; i++) {
				itemColor.push({ color: uniqueColors[i] });
			}
			return itemColor;
		},
		
		filterProducts: (state) => {
			return  state.filteredProduct.filter((product) => {
			if (!state.tagItems.length) return true;
				const Tags = state.tagItems.some((prev) => { // Match Tags
					if (product.tags) {
						if (product.tags.includes(prev)) {
							return prev;
						}
					}
				});
				return Tags;
			});
		},
		getOrder: (state) => {
			return state.order;
		}
	},
	actions:{
		setInitialCart(payload){
            this.cart = payload
          },
		grid2(payload){
			this.column2 = payload
			 this.column3 = false;
			this.column4 = false;
			this.column6 = false;
			this.listViewEnabled = false;
		 },
		 grid3() {
			 this.column2 = false;
			 this.column3 = true;
			 this.column4 = false;
			 this.column6 = false;
			 this.listViewEnabled = false;
		   },
		   grid4() {
			 this.column2 = false;
			 this.column3 = false;
			 this.column4 = true;
			 this.column6 = false;
			 this.listViewEnabled = false;
		   },
		   grid6() {
			 this.column2 = false;
			 this.column3 = false;
			 this.column4 = false;
			 this.column6 = true;
			 this.listViewEnabled = false;
		   },
		   listView() {
			 this.listViewEnabled = true;
			 this.list = true;
			 this.column2 = false;
			 this.column3 = false;
			 this.column4 = false;
			 this.column6 = false;
		   },
		   gridView() {
			 this.listViewEnabled = false;
			 this.column4 = true;
		   },
		 addToCart( payload)  {
			 let hasItems = this.cart.find(items => {
				 if (items.id === payload.id) {
					 items.quantity = items.quantity ? items.quantity : 1;
					 return true;
				 }
				 return false;
			 });
			 if (!hasItems) {
				 this.cart.push(payload);
			 }
			 if(process.client){
			 localStorage.setItem('cartItem', JSON.stringify(this.cart));
			 }
		 },
	 
		 updateCartQuantity (payload)  {
			 // Calculate Product stock Counts
			 function calculateStockCounts(product, quantity) {
				 let qty = product.quantity + quantity;
				 let stock = product.stock;
				 if (stock < qty) {
					 //   this.toastrService.error('You can not add more items than available. In stock '+ stock +' items.');
					 return false;
				 }
				 return true;
			 }
			 this.cart.find((items, index) => {
				 if (items.id === payload.product.id) {
	 
					 let qty = this.cart[index].quantity + payload.qty;
					 let stock = calculateStockCounts(this.cart[index], payload.qty);
					 if (qty !== 0 && stock)
						 this.cart[index]['quantity'] = qty;
						if(process.client){

							localStorage.setItem('cartItem', JSON.stringify(this.cart));
						}					 
					 return true;
				 }
			 });
		 },
	 
		 removeProduct( payload)  {
			 const index = this.cart.indexOf(payload);
			 this.cart.splice(index,1);
			 if(process.client){

				 localStorage.setItem('cartItem', JSON.stringify(this.cart));
			 }
		 },
	 
		 priceFilter( payload) {
			 this.filteredProduct = [];
			 this.products.forEach(product => {
				 if (product.price >= payload.min && product.price <= payload.max) {
					 this.filteredProduct.push(product);
				 }
			 });
	 
		 },
	 
		 setTags( payload)  {
			 this.tagItems = payload;
		 },
	 
		 sortProducts(payload)  {
			 if (payload === 'a-z') {
				 this.filteredProduct.sort(function (a, b) {
					 if (a.name < b.name) {
						 return -1;
					 } else if (a.name > b.name) {
						 return 1;
					 }
					 return 0;
				 });
			 } 
	
			   if (payload === 'low') {
				 this.filteredProduct.sort(function (a, b) {
					 if (a.price < b.price) {
						 return -1;
					 } else if (a.price > b.price) {
						 return 1;
					 }
					 return 0;
				 });
			 } else if (payload === 'high') {
				 this.filteredProduct.sort(function (a, b) {
					 if (a.price > b.price) {
						 return -1;
					 } else if (a.price < b.price) {
						 return 1;
					 }
					 return 0;
				 });
			 }
		 },
	 
		 createOrder(payload)  {
			 this.order = payload;
		 }	
	}
 })
 const cartItems = [];

