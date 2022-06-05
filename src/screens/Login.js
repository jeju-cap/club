import React from 'react';
import styled from 'styled-components/native';
import {View, Text, Button} from 'react-native';

const Container = styled.View`
flex: 1;
justify-content: center;
align-items: center;
background-color: ${({theme})=>theme.background};
`;

const Login = ({navigation})=>{
    return(
        <Container>
            <Text style={{fontSize:30}}>Login Screen</Text>
            <Button title="Signup" onPress={()=>navigation.navigate('signup')}/>
        </Container>
    );
};

export default Login;