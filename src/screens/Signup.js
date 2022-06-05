import React from 'react';
import styled from 'styled-components/native';

const Container = styled.View`
flex: 1;
justify-content: center;
align-items: center;
background-color: ${({theme})=>theme.background};
`;

const Signup = () => {
    return(
        <Container>
            <StyledText>Signup Screen</StyledText>
        </Container>
    );
};

export default Signup;