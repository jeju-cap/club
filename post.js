fetch("/signup",{
    method: "POST",
    headers: {
        "Content-Type":"application/json",
    },
    body: JSON.stringify({
        "id": this.state.name,
        "username": this.state.username,
        "password": this.state.password
    })
})
.then((response) => {
    if(response.status === 200){
        this.alert("Capzzang의 회원이 되신것을 축하드립니다!");
        this.props.history.push('/');
    }
    if(response.status === 401){
        this.alert("이미 존재하는 회원입니다.");
    }
    if(response.status === 400){
        this.alert("알 수 없는 오류가 발생했습니다.");
    }
})