import React from 'react';
import { Form, Input, Button } from 'antd';
import axios from 'axios';


export default class CustomForm extends React.Component {

    handleFormSubmit = (event, requestType, articleID) => {
        // event.preventDefault()
        const title = event.target.elements.title.value;
        const brief = event.target.elements.brief.value;
        const slug = event.target.elements.slug.value;
        
        switch (requestType){
            case 'post':
                return axios.post('http://127.0.0.1:8000/blog/api/',{
                    title : title,
                    brief : brief,
                    slug : slug
                })
                .then(res => console.log(res))
                .catch(err => console.log(err))
            case 'put':
                return axios.put(`http://127.0.0.1:8000/blog/api/${articleID}/`,{
                        title : title,
                        brief : brief,
                        slug : slug
                }).then(res => console.log(res)).catch(err => console.log(err))
                

            default:
                console.log(title,'---',brief,'----',slug)

        }
    }
    
    render() {
        return (
        <div>
            <Form onSubmit={(event) => this.handleFormSubmit(event, 
                this.props.requestType, this.props.articleID)}>
            <Form.Item label="Title">
                <Input name="title" placeholder="put the title" />
            </Form.Item>
            <Form.Item label="Slug">
                <Input name="slug" placeholder="put the slug" pattern="^[a-zA-Z0-9-]*$" />
            </Form.Item>
            <Form.Item label="Brief">
                <Input name="brief" placeholder="put your brief" />
            </Form.Item>
            <Form.Item>
            <Button type="primary" htmlType="submit">{this.props.btnText}</Button>
            </Form.Item>
            </Form>
        </div>
        );
    }
}